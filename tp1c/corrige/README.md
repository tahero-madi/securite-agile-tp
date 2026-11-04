# Corrigé du TP1-C

## Exemple d'objectif de sprint

> « Un agent peut créer, retrouver et suivre ses demandes, sans jamais voir celles des autres. »

Il est court, il porte de la valeur, et il intègre l'exigence de sécurité au lieu de la mettre à côté.

## DoR et DoD indicatives

| Definition of Ready (une story peut entrer en sprint si…) | Definition of Done (une story est terminée si…) |
| --- | --- |
| Les données manipulées sont identifiées et classées | Les tests, dont les tests de sécurité, sont verts dans le pipeline |
| Les critères de sécurité sont écrits en format testable | Les contrôles SAST, dépendances et secrets ne remontent aucun défaut bloquant |
| Les rôles autorisés sont précisés | La merge request est approuvée par une autre personne |
| Le besoin de modélisation des menaces est tranché | Aucun secret ni donnée réelle dans le code, les tests et les journaux |
| La story est estimée | Le modèle de menaces est mis à jour si la story change un flux |

**Critère à refuser :** « l'application est sécurisée ». Personne ne peut le vérifier, donc personne ne
peut dire qu'il n'est pas rempli.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
