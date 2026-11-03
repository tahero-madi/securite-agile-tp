# TP1-C — Sprint planning, Definition of Ready et Definition of Done

**Jour 1, 11:10 · 50 min · animé par le Scrum Master.** Objectif : planifier un premier sprint et écrire les
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

## Étape 3 — Daily Scrum avec une carte incident (10 min)

**Pourquoi.** Un sprint ne se déroule jamais comme prévu. Ce qui compte, c'est la façon dont l'équipe
décide face à un imprévu de sécurité.

Debout, 15 secondes par personne : hier, aujourd'hui, ce qui bloque. Puis le formateur tire une carte
incident. L'équipe décide et justifie :

- renégocier l'objectif de sprint avec le Product Owner ;
- traiter en **couloir d'urgence** Kanban ;
- ou mettre au backlog, avec une priorité.

## Étape 4 — Restitution croisée (10 min)

Chaque équipe présente sa DoD en 3 minutes. L'autre équipe cherche **un critère non vérifiable** et propose
de le reformuler.

## Point de contrôle

- Sprint 1 planifié : objectif écrit, tickets rattachés au jalon, 20 points au plus.
- DoR et DoD dans le README, chaque critère de sécurité vérifiable.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP2-A](../tp2a/README.md)
