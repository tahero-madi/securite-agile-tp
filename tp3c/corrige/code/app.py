"""Demandes internes : VERSION CORRIGEE (corrige formateur).

Corrections : requetes parametrees, controle d'acces sur chaque demande,
role gestionnaire pour la cloture, hachage scrypt, echappement HTML,
secrets hors du code, journaux sans mot de passe, en-tetes de securite.
Risque residuel volontaire pour l'audit : pas de jeton anti-CSRF.
"""
import os
import sqlite3

from flask import Flask, abort, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import config

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY or os.urandom(32)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE", "1") == "1",
)
app.config["DATABASE"] = config.DATABASE


# --- Base de donnees -------------------------------------------------------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def hash_password(password):
    return generate_password_hash(password)  # scrypt par defaut (Werkzeug 3)


def init_db():
    db = get_db()
    db.executescript(
        """
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS demandes;
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );
        CREATE TABLE demandes (
            id INTEGER PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            titre TEXT NOT NULL,
            description TEXT,
            statut TEXT NOT NULL DEFAULT 'ouverte'
        );
        """
    )
    users = [
        ("alice", "alice2026", "agent"),
        ("bob", "bob2026", "agent"),
        ("gestion", "gestion2026", "gestionnaire"),
    ]
    for username, password, role in users:
        db.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, hash_password(password), role),
        )
    demandes = [
        (1, "Acces VPN", "Ouverture d'un acces VPN pour teletravail"),
        (1, "Ecran supplementaire", "Second ecran pour le poste 214"),
        (2, "Badge perdu", "Remplacement du badge d'acces n. 4471"),
        (2, "Note de frais", "RIB : FR76 3000 6000 0112 3456 7890 189"),
    ]
    for owner_id, titre, description in demandes:
        db.execute(
            "INSERT INTO demandes (owner_id, titre, description) VALUES (?, ?, ?)",
            (owner_id, titre, description),
        )
    db.commit()


@app.cli.command("init-db")
def init_db_command():
    """Cree la base et les donnees de demonstration."""
    init_db()
    print("Base initialisee.")


# --- Authentification ------------------------------------------------------

def current_user():
    uid = session.get("user_id")
    if uid is None:
        return None
    return get_db().execute("SELECT * FROM users WHERE id = ?", (uid,)).fetchone()


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        user = get_db().execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]
            app.logger.info("Connexion reussie : %s", username)
            return redirect(url_for("index"))
        app.logger.warning("Echec de connexion pour le compte : %s", username)
        error = "Identifiant ou mot de passe incorrect"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# --- Demandes --------------------------------------------------------------

@app.route("/")
def index():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))
    q = request.args.get("q", "")
    db = get_db()
    if q:
        demandes = db.execute(
            "SELECT * FROM demandes WHERE owner_id = ? AND titre LIKE ?",
            (user["id"], f"%{q}%"),
        ).fetchall()
    else:
        demandes = db.execute(
            "SELECT * FROM demandes WHERE owner_id = ?", (user["id"],)
        ).fetchall()
    return render_template("index.html", user=user, demandes=demandes, q=q)


@app.route("/demandes/nouvelle", methods=["GET", "POST"])
def nouvelle_demande():
    user = current_user()
    if user is None:
        return redirect(url_for("login"))
    if request.method == "POST":
        titre = request.form.get("titre", "").strip()
        description = request.form.get("description", "")
        if not titre:
            return render_template("nouvelle.html", error="Le titre est obligatoire")
        db = get_db()
        db.execute(
            "INSERT INTO demandes (owner_id, titre, description) VALUES (?, ?, ?)",
            (user["id"], titre, description),
        )
        db.commit()
        return redirect(url_for("index"))
    return render_template("nouvelle.html", error=None)


@app.route("/demandes/<int:demande_id>")
def voir_demande(demande_id):
    user = current_user()
    if user is None:
        return redirect(url_for("login"))
    demande = get_db().execute(
        "SELECT * FROM demandes WHERE id = ?", (demande_id,)
    ).fetchone()
    # 404 plutot que 403 : on ne revele pas l'existence de la demande
    if demande is None or (
        demande["owner_id"] != user["id"] and user["role"] != "gestionnaire"
    ):
        abort(404)
    return render_template("demande.html", user=user, demande=demande)


@app.route("/demandes/<int:demande_id>/cloturer", methods=["POST"])
def cloturer_demande(demande_id):
    user = current_user()
    if user is None:
        return redirect(url_for("login"))
    if user["role"] != "gestionnaire":
        app.logger.warning("Cloture refusee : %s sur la demande %s", user["username"], demande_id)
        abort(403)
    db = get_db()
    db.execute("UPDATE demandes SET statut = 'cloturee' WHERE id = ?", (demande_id,))
    db.commit()
    return redirect(url_for("voir_demande", demande_id=demande_id))


@app.after_request
def entetes_securite(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; style-src 'self' 'unsafe-inline'; frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    return response


@app.route("/sante")
def sante():
    return {"statut": "ok"}


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
