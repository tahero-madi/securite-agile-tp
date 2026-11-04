# TP1-C — Sprint planning, Definition of Ready et Definition of Done

**Jour 1, 11:10 · 40 min · animé par le Scrum Master.** Objectif : planifier un premier sprint et écrire les
deux définitions qui font entrer la sécurité dans le cycle. Support : sections 1.2, 1.4 et 1.6.

## Étape 1 — Sprint Planning (15 min)

**Pourquoi.** Le Sprint Planning fixe ce que l'équipe s'engage à livrer, et pourquoi. C'est aussi le moment
de réserver de la capacité pour la sécurité, au lieu de la reporter au sprint suivant.

Le Scrum Master anime :

1. Le Product Owner propose un **objectif de sprint** en une phrase.
2. Capacité fictive de l'équipe : **20 points**.
3. L'équipe sélectionne les tickets du haut du backlog qui servent l'objectif, jusqu'à la capacité, et les
   rattache au jalon **Sprint 1**.

## Étape 2 — DoR et DoD (15 min)

**Pourquoi.** La **Definition of Ready** dit quand une story peut entrer en sprint ; la **Definition of
Done** dit quand elle est vraiment terminée. Ce sont les deux portes où la sécurité devient obligatoire.

Ajoutez au README deux sections, chacune avec **au moins 3 critères de sécurité** :

```markdown
## Definition of Ready
Une story peut entrer en sprint si :
- …

## Definition of Done
Une story est terminée si :
- …
```

**Règle d'or :** chaque critère doit être **vérifiable** par quelqu'un d'extérieur à l'équipe, avec une
preuve (un test, un rapport, une merge request).

## Étape 3 — Restitution : présenter sa DoD (10 min)

Chaque équipe présente sa Definition of Done en 3 minutes : quels critères de sécurité elle y a inscrits, et
comment chacun se vérifie — le test, le rapport ou la merge request qui le prouve.

## Point de contrôle

- Sprint 1 planifié : objectif écrit, tickets rattachés au jalon, 20 points au plus.
- DoR et DoD dans le README, chaque critère de sécurité vérifiable.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP2-A](../tp2a/README.md)
