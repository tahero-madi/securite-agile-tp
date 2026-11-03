"""Tests de securite (corrige formateur) : un test par critere d'acceptation."""
import logging


def test_un_agent_ne_voit_pas_la_demande_d_un_autre_agent(client, login):
    # Etant donne bob connecte, quand il ouvre la demande 1 d'alice, alors 404
    login("bob", "bob2026")
    assert client.get("/demandes/1").status_code == 404


def test_un_gestionnaire_voit_toutes_les_demandes(client, login):
    login("gestion", "gestion2026")
    assert client.get("/demandes/1").status_code == 200


def test_un_agent_ne_peut_pas_cloturer(client, login):
    login("alice", "alice2026")
    assert client.post("/demandes/1/cloturer").status_code == 403
    assert "ouverte" in client.get("/demandes/1").get_data(as_text=True)


def test_un_gestionnaire_peut_cloturer(client, login):
    login("gestion", "gestion2026")
    client.post("/demandes/3/cloturer")
    assert "cloturee" in client.get("/demandes/3").get_data(as_text=True)


def test_la_recherche_resiste_a_l_injection_sql(client, login):
    login("alice", "alice2026")
    page = client.get("/?q=' OR 1=1 --").get_data(as_text=True)
    assert "Badge perdu" not in page and "Note de frais" not in page


def test_la_description_est_echappee(client, login):
    login("alice", "alice2026")
    client.post("/demandes/nouvelle",
                data={"titre": "XSS", "description": "<script>alert(1)</script>"})
    page = client.get("/demandes/5").get_data(as_text=True)
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;" in page


def test_aucun_mot_de_passe_dans_les_journaux(login, caplog):
    with caplog.at_level(logging.INFO):
        login("alice", "MotDePasseTest!")
    assert "MotDePasseTest!" not in caplog.text


def test_mots_de_passe_haches_avec_un_algorithme_adapte(app):
    from app import get_db
    with app.app_context():
        h = get_db().execute("SELECT password FROM users").fetchone()["password"]
    assert h.startswith(("scrypt:", "pbkdf2:"))
