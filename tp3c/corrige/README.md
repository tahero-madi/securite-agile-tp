# Corrigé du TP3-C

Le dossier [`code/`](code/) contient les fichiers corrigés. Copiés par-dessus le projet fourni, ils donnent
**14 tests verts** (6 fonctionnels, 8 de sécurité), et Bandit, Semgrep et pip-audit ne remontent plus rien
(vérifié le 1er novembre 2026).

| Fichier | Rôle |
| --- | --- |
| [`requirements.txt`](code/requirements.txt) | Flask 3.1.3, Werkzeug 3.1.9, Jinja2 3.1.6 |
| [`config.py`](code/config.py) | Plus aucun secret : tout vient de l'environnement |
| [`.gitleaksignore`](code/.gitleaksignore) | Modèle pour documenter le jeton révoqué |
| [`app.py`](code/app.py) | L'application corrigée |
| [`templates/demande.html`](code/templates/demande.html) | Description échappée, sans `| safe` |
| [`tests/test_securite.py`](code/tests/test_securite.py) | Un test par critère d'acceptation |
| [`.gitlab-ci.yml`](code/.gitlab-ci.yml) | Les quatre contrôles actifs et bloquants |
| [`Dockerfile`](code/Dockerfile) | Image minimale, utilisateur non root |

## L'ordre conseillé, et pourquoi

### 1. Les dépendances

```text
Flask==3.1.3
Werkzeug==3.1.9
Jinja2==3.1.6
```

C'est la correction la plus rapide et elle fait tomber d'un coup les 27 alertes de pip-audit. Elle passe en
premier parce que `generate_password_hash` (étape 3) repose sur Werkzeug.

### 2. Les secrets

`config.py` lit `SECRET_KEY` et `NOTIF_API_TOKEN` dans l'environnement : en CI, ce sont des variables
masquées et protégées. Le jeton reste pourtant dans l'historique, et Gitleaks continue de le voir. La seule
réponse correcte : **révoquer** le jeton, puis consigner son empreinte (champ `Fingerprint` du rapport) dans
`.gitleaksignore`, avec la date et le ticket :

```text
# Jeton de notification revoque le 03/11/2026 (ticket SEC-06)
<commit>:config.py:gitlab-pat:8
```

Réécrire l'historique (`git filter-repo`) ne suffit pas : chaque clone fait avant la réécriture garde le
jeton. Une fois révoqué, il ne vaut plus rien, où qu'il soit.

### 3. Le code

```python
# Injection SQL (SEC-03) : la saisie devient un paramètre, jamais du SQL
demandes = db.execute(
    "SELECT * FROM demandes WHERE owner_id = ? AND titre LIKE ?",
    (user["id"], f"%{q}%"),
).fetchall()

# Hachage (SEC-05) : scrypt par défaut avec Werkzeug 3
from werkzeug.security import check_password_hash, generate_password_hash
user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
if user and check_password_hash(user["password"], password):
    ...

# Journal (SEC-05) : l'identifiant, jamais le mot de passe
app.logger.warning("Echec de connexion pour le compte : %s", username)

# Debug et adresse d'écoute pilotés par l'environnement
app.run(host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG") == "1")
```

Et dans `templates/demande.html`, `{{ demande.description }}` sans `| safe` (SEC-04) : Jinja échappe le HTML
de lui-même.

### 4. Le contrôle d'accès

```python
# Consultation (SEC-01) : 404 plutôt que 403, on ne révèle pas que la demande existe
if demande is None or (
    demande["owner_id"] != user["id"] and user["role"] != "gestionnaire"
):
    abort(404)

# Clôture (SEC-02) : action réservée au rôle gestionnaire, tentative tracée
if user["role"] != "gestionnaire":
    app.logger.warning("Cloture refusee : %s sur la demande %s", user["username"], demande_id)
    abort(403)
```

Ce sont les deux corrections qu'**aucun scanner** n'aurait demandées. Elles ne sont prouvées que par les
tests `test_un_agent_ne_voit_pas_la_demande_d_un_autre_agent` et `test_un_agent_ne_peut_pas_cloturer`.

### En plus

Le corrigé ajoute des **en-têtes de sécurité** (CSP, `X-Frame-Options`, `X-Content-Type-Options`) et des
**cookies de session** `HttpOnly`, `SameSite=Lax` et `Secure` : ZAP les réclamera au TP4-A.

## Ce qui reste volontairement ouvert

**Aucun jeton anti-CSRF** sur les formulaires. Ce risque résiduel est laissé pour l'audit du TP4-A : si vos
auditeurs le trouvent, ils ont bien travaillé.

## Si le temps a manqué

Le minimum attendu : dépendances à jour, une faille de code corrigée, un test de sécurité vert. Le reste
part au backlog avec un ticket et un délai : c'est exactement ce qu'on attend d'une équipe agile, et c'est ce
que l'audit regardera.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
