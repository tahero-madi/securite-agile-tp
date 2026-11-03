# TP4-B — Registre de risques et plan de remédiation

**Jour 2, 14:45 · 40 min · chaque équipe sur son propre projet, avec les constats reçus.** Objectif :
transformer menaces et constats en décisions : traiter, accepter, et prévoir le sprint suivant. Support :
sections 4.2, 4.4 et 4.5. Modèles : `docs/modeles/03-registre-des-risques.csv`, `05-plan-donnees-sensibles.md`,
`06-plan-remediation.md`.

## Étape 1 — Le registre de risques (15 min)

**Pourquoi.** Le registre est la mémoire des risques de l'équipe : ce qui est connu, ce qui est traité, ce
qui est accepté et par qui. En agile, il vit à côté du backlog : chaque risque à réduire y a son ticket.

Copiez `03-registre-des-risques.csv` en `docs/registre-des-risques.csv`. Ouvrez-le dans un tableur ou
directement dans GitLab (séparateur point-virgule). Fusionnez :

- les menaces du TP2-A **encore ouvertes** ;
- les **constats d'audit** reçus (tickets `AUDIT-`).

Pour chacun : formulez le risque en **cause → événement → conséquence**, cotez vraisemblance et impact de 1
à 4, calculez le score, puis choisissez un traitement :

| Traitement | Quand |
| --- | --- |
| Réduire | Une mesure existe et son coût est raisonnable : elle devient une story |
| Transférer | Un tiers porte le risque (assurance, prestataire, hébergeur) |
| Éviter | On renonce à la fonctionnalité qui crée le risque |
| Accepter | Le risque est faible ou la mesure trop coûteuse : **décision signée par le Product Owner**, avec une date de réexamen |

## Étape 2 — Le plan des données sensibles (10 min)

**Pourquoi.** Une donnée sensible fuit rarement là où on l'attend : plus souvent dans un journal, une
sauvegarde, un export ou un jeu de test qu'à travers l'écran principal.

Copiez `05-plan-donnees-sensibles.md` en `docs/plan-donnees-sensibles.md`. Pour chaque donnée (mot de
passe, RIB dans une demande, identité de l'agent…) : sa classification, **tous les endroits où elle passe**,
la mesure qui s'applique à chacun, et sa durée de conservation.

## Étape 3 — Le plan de remédiation (15 min)

Copiez `06-plan-remediation.md` en `docs/plan-remediation.md`.

1. Créez le jalon **Sprint 2**.
2. Pour chaque risque à réduire, une story dans le jalon, avec sa **preuve de clôture** attendue.
3. Indiquez la part de la capacité réservée à la sécurité.
4. Listez les risques acceptés, avec la justification, la signature du Product Owner et la date de réexamen.

## Point de contrôle

Chaque risque a un traitement et une action ; tout risque accepté est signé par le Product Owner.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP4-C](../tp4c/README.md)
