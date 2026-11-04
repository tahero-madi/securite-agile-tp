# TP1-B — Le backlog et ses abuse cases

**Jour 1, 10:35 · 35 min · par équipe.** Objectif : construire un backlog estimé et ordonné, où la sécurité
apparaît dès le départ sous forme d'abuse cases. Support : section 1.5. Modèle :
`docs/modeles/01-user-story-securite.md` de votre projet.

**Vision produit :** *permettre aux agents de déposer et suivre leurs demandes internes, et aux gestionnaires
de les traiter, sans exposer les données d'un agent à un autre.*

## Étape 1 — Les user stories (15 min)

**Pourquoi.** Une user story décrit un besoin du point de vue de l'utilisateur, avec un critère qui dit
quand il est satisfait. Une bonne story est INVEST : indépendante, négociable, porteuse de valeur, estimable,
petite (*small*), testable.

Rédigez **6 à 8 stories**, chacune dans un ticket : **Planifier > Éléments de travail** (Plan > **Work items**,
anciennement *Tickets / Issues*), bouton **Nouveau** puis type **Issue**.

- **Titre :** « En tant que …, je veux …, afin de … ».
- **Description :** au moins un critère d'acceptation.
- **Labels :** `type::story` et `etat::a-faire` ; ajoutez `donnees::sensibles` si la story en manipule.
- **Jalon :** laissez vide pour l'instant (TP1-C).

Pensez aux deux rôles de l'application : l'agent (créer, consulter, rechercher ses demandes) et le
gestionnaire (consulter toutes les demandes, les clôturer).

## Étape 2 — Les abuse cases (10 min)

**Pourquoi.** Un abuse case retourne une story du point de vue de l'attaquant. Il produit un **critère
négatif** : ce que le système doit refuser. Sans lui, personne ne teste ce qui ne doit pas marcher.

Ajoutez **au moins 2 abuse cases**, labels `type::abuse-case` **et `etat::a-faire`** (un abuse case est un
ticket qui vit sur le tableau, comme une story), plus `risque::eleve` ou `risque::moyen` selon la gravité :

```text
En tant qu'agent malveillant, je veux <action interdite>, afin de <gain pour l'attaquant>.

Critère d'acceptation (négatif) : <ce que le système doit répondre>
```

Inspirez-vous de la démonstration de ce matin.

## Étape 3 — Estimer en planning poker (5 min)

**Pourquoi.** Estimer à plusieurs fait apparaître les désaccords, et donc les risques oubliés : celui qui
annonce 8 quand les autres disent 2 a souvent vu un problème de sécurité.

Pour chaque ticket, chacun annonce en même temps une valeur de la suite **1, 2, 3, 5, 8, 13**. Si deux
annonces sont séparées de plus de deux valeurs, les extrêmes s'expliquent, puis on revote. Notez le résultat
dans la description du ticket : `Estimation : 5 points`.

## Étape 4 — Prioriser en MoSCoW (5 min)

Le Product Owner classe chaque ticket en *Must*, *Should*, *Could* ou *Won't*, puis ordonne la colonne
`etat::a-faire` du tableau par glisser-déposer : **l'ordre du tableau est l'ordre du backlog.**

## Point de contrôle

- Le backlog contient 6 à 8 stories estimées et ordonnées.
- Au moins 2 abuse cases, chacun avec un critère négatif, **présents sur le tableau** (`etat::a-faire`) et
  estimés comme les stories.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP1-C](../tp1c/README.md)
