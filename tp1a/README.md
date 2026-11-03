# TP1-A — Le projet, le tableau, les labels

**Jour 1, 10:05 · 30 min · par équipe.** Objectif : installer dans GitLab l'outillage agile de votre équipe,
avec dès le départ une place pour la sécurité. Support : sections 1.2 à 1.4.

Tout se fait dans le navigateur, dans le projet GitLab de votre équipe. Si ce n'est pas déjà fait, suivez
l'étape 1 de [Avant de commencer](../avant-de-commencer.md).

## Étape 1 — Choisir vos rôles (5 min)

**Pourquoi.** Une équipe agile a besoin que quelqu'un porte la valeur, quelqu'un le cadre et quelqu'un la
sécurité. Ce sont les rôles du projet fil rouge, pas vos postes réels : choisissez-les librement.

| Rôle | Ce qu'il fait pendant les TP |
| --- | --- |
| Product Owner | Ordonne le backlog, tranche les priorités, signe les risques acceptés |
| Scrum Master | Anime le Sprint Planning, le Daily et les restitutions, garde le temps, fait respecter les règles |
| Champion sécurité | Relaie les bonnes pratiques, anime la modélisation des menaces, aide au tri des alertes |

Tout le monde reste développeur : chacun code, teste et relit au jour 2. Vous pourrez changer de rôle au
jour 2.

**Et pour votre compte :** activez la double authentification si ce n'est pas fait (recommandé), en suivant
[Avant de commencer](../avant-de-commencer.md#1-votre-compte-gitlab). Un compte de développeur compromis,
c'est un dépôt compromis.

## Étape 2 — Les labels

**Pourquoi.** Les labels rendent la sécurité visible dans le backlog : le Product Owner voit d'un coup d'œil
les stories qui touchent des données sensibles ou qui portent un risque élevé.

Menu **Gérer > Labels** (Manage > Labels), **Nouveau label**, une fois pour chacun :

| Famille | Labels |
| --- | --- |
| Type | `type::story`, `type::securite`, `type::abuse-case` |
| Risque | `risque::eleve`, `risque::moyen`, `risque::faible` |
| Données | `donnees::sensibles` |
| État (colonnes du tableau) | `etat::a-faire`, `etat::en-cours`, `etat::en-revue` |

Choisissez une couleur par famille, par exemple rouge pour le risque et violet pour les données.

> Dans l'édition gratuite de GitLab, les deux-points `::` sont un simple séparateur : un ticket peut porter
> deux labels `risque::` à la fois. C'est à l'équipe de s'en tenir à un seul.

## Étape 3 — Le tableau

**Pourquoi.** Le tableau rend le flux visible ; limiter le travail en cours évite d'avoir tout commencé et
rien terminé.

1. Menu **Planifier > Tableaux des tickets** (Plan > Issue boards).
2. Ajoutez trois listes, dans cet ordre, avec **Créer une liste** : `etat::a-faire`, `etat::en-cours`,
   `etat::en-revue`. Les listes **Open** et **Closed** restent aux extrémités.
3. **Limite de travail en cours :** au plus **2 tickets** dans « En cours ». L'édition gratuite de GitLab
   n'affiche pas de limite sur la liste : écrivez cette règle dans le README (étape 5), le Scrum Master la
   fait respecter.

## Étape 4 — Le jalon « Sprint 1 »

Menu **Planifier > Jalons** (Plan > Milestones), **Nouveau jalon** : titre `Sprint 1`, date de début
aujourd'hui, date de fin dans deux semaines (durée fictive).

## Étape 5 — Les règles de l'équipe dans le README

Ouvrez `README.md` à la racine du projet, cliquez sur **Modifier > Modifier un fichier** (Edit > Edit single
file) et ajoutez à la fin :

```markdown
## Équipe

| Rôle | Nom |
| --- | --- |
| Product Owner | … |
| Scrum Master | … |
| Champion sécurité | … |

## Règles de fonctionnement

- Au plus 2 tickets dans la colonne « En cours ».
- Toute merge request est relue par une autre personne que son auteur.
- Aucun secret ni donnée réelle dans le code, les tickets ou les captures d'écran.
```

Validez avec un message de commit explicite, par exemple « Rôles et règles de l'équipe ».

## Point de contrôle

- Le tableau affiche les trois colonnes et les labels existent.
- Les rôles choisis par l'équipe et ses règles sont écrits dans le README.

**À débattre en équipe :** en quoi le label `donnees::sensibles` aide-t-il le Product Owner à prioriser ?

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP1-B](../tp1b/README.md)
