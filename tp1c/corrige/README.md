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

## Les cartes incident : réponses attendues

| Carte | Décision attendue | Pourquoi |
| --- | --- | --- |
| « Un jeton d'API a été collé dans un ticket public » | Couloir d'urgence : **révoquer le jeton d'abord**, puis nettoyer le ticket et chercher d'autres fuites | Le jeton est compromis dès qu'il est visible ; le supprimer du ticket ne suffit pas |
| « Le RSSI signale une vulnérabilité critique sur Werkzeug » | Évaluer en minutes : sommes-nous exposés, est-elle exploitée (catalogue KEV, EPSS) ? Si oui, couloir d'urgence ; sinon, ticket priorisé dans le sprint | On décide sur l'exploitation réelle et l'exposition, pas sur le seul score CVSS (module 4) |

Dans les deux cas, le Product Owner est informé : si l'urgence consomme la capacité, l'objectif de sprint
se renégocie avec lui, il ne se dégrade pas en silence.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
