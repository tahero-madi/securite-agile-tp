# Corrigé du TP2-C

## L'ordre attendu en tête du backlog

| Rang | Story | Score de la menace | Preuve de clôture |
| --- | --- | --- | --- |
| 1 | SEC-01 — Mes demandes ne sont visibles que par moi et les gestionnaires | 12 (M-01) | Test automatisé |
| 2 | SEC-03 — La recherche ne lit que mes données | 12 (M-02) | Test automatisé, et Bandit / Semgrep dans le pipeline |
| 3 | SEC-02 — Seul un gestionnaire clôture | 8 (M-03) | Test automatisé |
| 4 | SEC-04 — Le texte des demandes est échappé | 9 (M-04) | Test automatisé, et Semgrep |
| 5 | SEC-05 — Mots de passe hachés et absents des journaux | 8–9 (M-05, M-07) | Test automatisé, et Semgrep |
| 6 | SEC-06 — Aucun secret dans le dépôt | 9 (M-06) | Contrôle du pipeline : Gitleaks |

SEC-02 peut passer avant SEC-04 malgré un score plus faible : elle est petite et touche le même code que
SEC-01. Le Product Owner a le droit d'arbitrer, **à condition que les deux menaces critiques (12) restent en
tête.**

## Les preuves : pourquoi ces choix

- **Test automatisé** pour SEC-01 à SEC-05 : chacun de leurs critères dit quoi saisir et quoi attendre, donc
  il s'écrit en quelques lignes de pytest. Il échouera tant que la faille existe, puis empêchera qu'elle
  revienne.
- **Contrôle du pipeline** pour SEC-06 : on ne teste pas l'absence de secret avec un test unitaire, on fait
  lire tout l'historique par Gitleaks à chaque modification.
- La **revue de code** et le **test manuel** restent utiles, mais ne se rejouent pas d'eux-mêmes : ce sont
  des preuves de second rang.

Demain, au TP3-C, ces lignes « Preuve de clôture » deviennent votre liste de travail.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
