# Corrigé du TP3-A

## Les réponses sur `.gitlab-ci.yml`

1. **Trois étapes** : `tests`, `securite`, `dast`, exécutées dans cet ordre.
2. **Un seul job actif**, `tests`. Les jobs dont le nom commence par un point (`.sast-bandit`…) sont des
   jobs **cachés** : GitLab les lit mais ne les exécute pas. Retirer le point les active (TP3-B).
3. **Les images** : `python:3.12-slim` par défaut, `zricethezav/gitleaks:v8.26.0`,
   `ghcr.io/zaproxy/zaproxy:stable`, et `sonarsource/sonar-scanner-cli:latest` pour le job SonarQube
   facultatif.
4. **Pourquoi épingler.** Pour que le pipeline d'aujourd'hui donne le même résultat que celui de demain, et
   pour ne pas exécuter sans le savoir une nouvelle version, éventuellement piégée. En mars 2026, l'action
   GitHub de Trivy, un scanner de sécurité, a vu 75 de ses 76 étiquettes déplacées vers un code qui volait
   les secrets des pipelines : tous ceux qui pointaient sur une étiquette ont exécuté ce code.
   **Non épinglées :** `zaproxy:stable` et surtout `sonar-scanner-cli:latest`, qui changent sans prévenir.
   En production, on épingle même par empreinte : `image@sha256:…`, qu'aucune étiquette déplacée ne peut
   détourner.

## Les réglages attendus

| Réglage | Valeur |
| --- | --- |
| Branche protégée `main` | Fusion : Maintainers · Push : Personne · Force push : désactivé |
| Merge checks | « Le pipeline doit réussir » coché |
| Variable `SECRET_KEY` | Masquée, protégée, valeur aléatoire de 64 caractères hexadécimaux |

## Les questions qui reviennent

- **« Ma variable `SECRET_KEY` est vide dans le job de ma branche. »** C'est voulu : protégée, elle n'est
  transmise qu'aux branches protégées, donc pas à `securite/pipeline`. Un job lancé depuis une branche de
  travail ne doit pas pouvoir lire les secrets de production. Le job `dast-zap` du TP4-A fabrique sa propre
  clé de test pour cette raison.
- **« Pourquoi personne ne peut pousser, même pas les Maintainers ? »** Pour que chaque changement passe par
  une merge request, donc par le pipeline et par une relecture. Un Maintainer peut toujours fusionner, mais
  plus contourner.
- **« L'édition gratuite peut-elle imposer une approbation ? »** Non : les règles d'approbation obligatoires
  sont une fonction payante de GitLab. La relecture par un pair reste une règle de la Definition of Done,
  que l'audit du TP4-A vérifiera dans l'historique des merge requests.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
