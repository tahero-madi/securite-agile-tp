# Corrigé du TP3-B

## Ce que trouvent les outils

Résultats sur l'application fournie, vérifiés le 1er novembre 2026 :

| Outil | Résultat |
| --- | --- |
| Bandit | **6 défauts** : MD5 (B324, élevé), debug Flask (B201, élevé), SQL construit par formatage (B608, moyen), écoute sur 0.0.0.0 (B104, moyen), 2 secrets en dur (B105, faible) |
| Semgrep (règles du dépôt, `.semgrep/`) | **5 défauts** : SQL construit, MD5, debug actif, mot de passe dans un journal, filtre `safe` |
| pip-audit | **27 vulnérabilités connues** ou plus sur Flask 3.0.0, Werkzeug 3.0.0 et Jinja2 3.1.2 ; le nombre augmente avec le temps |
| Gitleaks | **1 secret** : le jeton `glpat-` fictif de `config.py` |
| CycloneDX | Un SBOM de **3 composants** : ce n'est pas un contrôle, c'est un inventaire |

## Le tableau de tri attendu

| Outil | Défaut | Fichier | Vrai / faux | Criticité | Menace |
| --- | --- | --- | --- | --- | --- |
| Bandit B608, Semgrep | SQL construit par formatage | `app.py`, recherche | Vrai | Critique | M-02 |
| Semgrep | Filtre `safe` sur la description | `templates/demande.html` | Vrai | Élevée | M-04 |
| Bandit B324, Semgrep | Mots de passe en MD5 | `app.py`, `hash_password` | Vrai | Élevée | M-05 |
| Semgrep | Mot de passe écrit dans le journal | `app.py`, `login` | Vrai | Élevée | M-07 |
| Gitleaks, Bandit B105 | Jeton d'API dans le code et l'historique | `config.py` | Vrai | Élevée | M-06 |
| Bandit B105 | `SECRET_KEY` en dur | `config.py` | Vrai | Élevée | M-06 |
| Bandit B201, Semgrep | `debug=True` | `app.py` | Vrai | Élevée | (nouvelle : A02) |
| Bandit B104 | Écoute sur 0.0.0.0 | `app.py` | **Discutable** : nécessaire dans un conteneur, à piloter par une variable | Moyenne | — |
| pip-audit | Flask, Werkzeug, Jinja2 vulnérables | `requirements.txt` | Vrai | Élevée | (nouvelle : A03) |

## Les réponses aux questions

- **Où Gitleaks a-t-il trouvé le jeton ?** Dans l'**historique** Git, au commit « Version initiale ». Le job
  clone tout l'historique (`GIT_DEPTH: "0"`) : supprimer la ligne du code ne suffira donc pas (TP3-C).
- **Quel outil a détecté M-01 ?** **Aucun.** Ni M-03. Un scanner voit des motifs dans le code (une requête
  construite par concaténation, une fonction de hachage faible) ; il ne sait pas qu'« un agent ne doit voir
  que ses demandes ». L'autorisation est une règle métier : elle se prouve par les **tests écrits depuis les
  stories**, et c'est l'objet du TP3-C.

## Discussion sur les seuils

B608 (SQL construit) a une **confiance faible** chez Bandit : avec le seuil du pipeline (sévérité et
confiance au moins moyennes), Bandit ne bloquera pas dessus, alors que Semgrep si. Deux outils de la même
famille ne voient pas la même chose avec les mêmes réglages : c'est pourquoi on les combine, et pourquoi on
choisit ses seuils en connaissance de cause.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
