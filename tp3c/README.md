# TP3-C — Pipeline rouge : trier, corriger, relancer

**Jour 2, 11:10 · 50 min · par équipe. Mise en situation évaluée.** Objectif : faire des contrôles une vraie
barrière, puis corriger jusqu'au vert, en prouvant chaque correction par un test. Support : sections 3.2,
3.7 et 3.8.

Travaillez sur la branche `securite/pipeline` et sa merge request. Sur votre VM :

```bash
cd ~/equipe-a && git switch securite/pipeline && git pull
. .venv/bin/activate
```

## Étape 1 — Rendre les contrôles bloquants (5 min)

**Pourquoi.** En observation, un contrôle informe ; bloquant, il empêche la fusion. C'est ce qui transforme
la Definition of Done en règle appliquée par la machine.

Dans `.gitlab-ci.yml`, passez `allow_failure` à `false` sur les quatre contrôles : `secrets-gitleaks`,
`sast-bandit`, `sast-semgrep`, `sca-pip-audit`. Validez et poussez : le pipeline devient **rouge** et le
bouton **Merge** de la merge request se grise.

## Étape 2 — Trier (10 min)

**Pourquoi.** Tout ne se corrige pas dans l'heure. Une équipe agile décide ce qui est traité maintenant et
ce qui part au backlog, avec un délai, plutôt que de tout désactiver pour retrouver le vert.

À partir de votre tableau du TP3-B, créez **un ticket par groupe de défauts** (label `type::securite`, un
label `risque::`, le délai dans la description) et décidez : corrigé maintenant, ou backlog avec délai.

## Étape 3 — Écrire les tests de sécurité d'abord (10 min)

**Pourquoi.** Un test écrit avant la correction doit **échouer** : c'est la preuve qu'il détecte bien la
faille. Une fois la correction faite, il passe, et il empêchera la faille de revenir.

Ouvrez `tests/test_securite.py` et remplacez le squelette par un test par critère d'acceptation de SEC-01 à
SEC-05, en reprenant vos scénarios Étant donné / Quand / Alors. Les fixtures `client` et `login` sont
fournies par `tests/conftest.py`. Exemple pour SEC-01 :

```python
def test_un_agent_ne_voit_pas_la_demande_d_un_autre_agent(client, login):
    login("bob", "bob2026")                                   # Étant donné bob connecté
    reponse = client.get("/demandes/1")                       # Quand il ouvre la demande d'alice
    assert reponse.status_code == 404                         # Alors il reçoit une 404
```

```bash
python -m pytest tests/test_securite.py -v        # vos tests doivent échouer : c'est voulu
```

## Étape 4 — Corriger (20 min)

Répartissez-vous le travail en trois lots :

| Lot | Contenu | Fichiers |
| --- | --- | --- |
| 1. Dépendances et secrets | Mettre à jour Flask, Werkzeug et Jinja2 ; lire `SECRET_KEY` et le jeton depuis l'environnement ; traiter le jeton présent dans l'historique | `requirements.txt`, `config.py`, `.gitleaksignore` |
| 2. Code | Requête SQL paramétrée ; hachage adapté (`generate_password_hash`) ; plus de mot de passe dans le journal ; `debug` et l'adresse d'écoute pilotés par variables d'environnement ; retirer `| safe` | `app.py`, `templates/demande.html` |
| 3. Contrôle d'accès | Une demande n'est visible que par son auteur ou un gestionnaire (sinon 404) ; seul un gestionnaire clôture (sinon 403) | `app.py`, `voir_demande` et `cloturer_demande` |

Après chaque correction :

```bash
python -m pytest                                  # tous les tests
bandit -r . -x ./tests,./.venv --severity-level medium --confidence-level medium
git add -A && git commit -m "SEC-0x : <ce qui est corrigé>" && git push
```

**Le cas du jeton dans l'historique.** Supprimer la ligne de `config.py` ne suffit pas : Gitleaks lit tout
l'historique, et chaque clone en garde une copie. La bonne réponse se fait en deux temps :

1. **Révoquer** le jeton auprès du service qui l'a émis (ici, annoncez-le : le jeton est fictif).
2. **Documenter** l'exception : copiez le champ `Fingerprint` du rapport Gitleaks dans `.gitleaksignore`,
   avec en commentaire la date de révocation et le ticket.

## Étape 5 — Pipeline vert, fusion (5 min)

Quand le pipeline de la merge request est vert, un **autre membre de l'équipe** relit la merge request et
fusionne dans `main`.

## Point de contrôle

**Minimum :** dépendances à jour, une faille de code corrigée, un test de sécurité vert.
**Objectif :** pipeline vert avec les quatre contrôles bloquants, et SEC-01 à SEC-05 couvertes par un test.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP4-A](../tp4a/README.md)
