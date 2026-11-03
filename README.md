# Développer de manière sécurisée et agile · Travaux pratiques

Formation 3-033, deux jours. Douze travaux pratiques en équipe, sur une application web volontairement
vulnérable, « Demandes internes ». Vous la faites évoluer comme une vraie équipe agile : backlog, menaces,
security user stories, pipeline DevSecOps, audit et comité de mise en production.

## Comment travailler

- **Lisez l'énoncé ici**, sur GitHub, dans le navigateur de votre poste. Chaque bloc de commandes a un
  bouton de copie en haut à droite.
- **Travaillez dans GitLab** : https://gitlab-3033.mooo.com, groupe `formation-3033`, projet de votre
  équipe (`equipe-a` ou `equipe-b`). Le backlog, le tableau, le code et le pipeline y sont.
- **Codez sur votre VM** (à partir du TP3-A), en SSH ou avec VS Code Remote-SSH.
- Commencez par [Avant de commencer](avant-de-commencer.md) : votre compte GitLab, votre VM et le jeton
  d'accès pour Git.

## Corrigés

Chaque TP a son corrigé dans un sous-dossier `corrige/` : `tp2a/corrige/` pour le TP2-A, par exemple. Il
contient les réponses attendues et, pour le TP3-C, le code corrigé de l'application.

Vous êtes des professionnels : cherchez d'abord en équipe, ouvrez le corrigé pour vous débloquer ou pour
comparer à la fin du TP. Un corrigé lu trop tôt vous prive de la discussion, qui est l'essentiel du TP.

## Programme des TP

| Quand | TP | Durée |
| --- | --- | --- |
| **Jour 1 · Module 1 — Agilité et points d'entrée de la sécurité** | | |
| Jour 1, 10:05 | [TP1-A — Le projet, le tableau, les labels](tp1a/README.md) | 30 min |
| Jour 1, 10:35 | [TP1-B — Le backlog et ses abuse cases](tp1b/README.md) | 35 min |
| Jour 1, 11:10 | [TP1-C — Sprint planning, Definition of Ready et Definition of Done](tp1c/README.md) | 50 min |
| **Jour 1 · Module 2 — La sécurité dans les projets agiles** | | |
| Jour 1, 13:50 | [TP2-A — Modéliser les menaces de l'application](tp2a/README.md) | 50 min |
| Jour 1, 14:40 | [TP2-B — Écrire les security user stories](tp2b/README.md) | 40 min |
| Jour 1, 15:20 | [TP2-C — Re-prioriser et préparer la validation](tp2c/README.md) | 25 min |
| **Jour 2 · Module 3 — Pratiques de sécurité dans les outils agiles** | | |
| Jour 2, 09:55 | [TP3-A — Protéger le dépôt, lancer le pipeline](tp3a/README.md) | 30 min |
| Jour 2, 10:25 | [TP3-B — Activer les contrôles, lire les rapports](tp3b/README.md) | 45 min |
| Jour 2, 11:10 | [TP3-C — Pipeline rouge : trier, corriger, relancer](tp3c/README.md) | 50 min |
| **Jour 2 · Module 4 — Suivi, audit et gestion des risques** | | |
| Jour 2, 14:00 | [TP4-A — Audit croisé](tp4a/README.md) | 45 min |
| Jour 2, 14:45 | [TP4-B — Registre de risques et plan de remédiation](tp4b/README.md) | 40 min |
| Jour 2, 15:25 | [TP4-C — Comité « go / no-go »](tp4c/README.md) | 20 min |

En fin de formation : [QCM final](qcm-final.md). En cas de problème : [En cas de blocage](en-cas-de-blocage.md).

## Les équipes et les rôles

Deux équipes de trois, chacune avec son projet GitLab. Les rôles sont annoncés le premier matin.

| Rôle | Ce qu'il fait pendant les TP |
| --- | --- |
| Product Owner | Ordonne le backlog, tranche les priorités, signe les risques acceptés |
| Scrum Master | Anime le Sprint Planning, le Daily et la restitution, garde le temps |
| Champion sécurité | Relaie les bonnes pratiques, anime la modélisation des menaces, aide au tri des alertes |

Dans GitLab, vous êtes **Maintainer** sur le projet de votre équipe et **Reporter** (lecture seule) sur celui
de l'autre équipe : c'est ce qui permet l'audit croisé du TP4-A.

## Le fil conducteur

Une faille vue en démonstration le premier matin devient une **menace** (TP2-A), puis une **story** avec un
critère testable (TP2-B), puis un **test** qui fait échouer le pipeline (TP3-C), puis une **preuve** d'audit
(TP4-A). Gardez vos livrables d'un TP à l'autre : chacun sert au suivant.

## Contenu du dépôt

| Élément | Contenu |
| --- | --- |
| `tp1a/` à `tp4c/` | L'énoncé du TP (`README.md`) et son corrigé (`corrige/`) |
| `tp3c/corrige/code/` | Les fichiers corrigés de l'application, à comparer avec les vôtres |
| `avant-de-commencer.md` | Compte GitLab, VM, jeton d'accès, premier clone |
| `en-cas-de-blocage.md` | Les problèmes courants et leur solution |
| `qcm-final.md` | Les consignes du QCM final |

Les **modèles de livrables** (user story, modèle de menaces, registre de risques, grille d'audit, plan des
données sensibles, plan de remédiation) sont dans votre projet GitLab, dossier `docs/modeles/` : vous les
remplissez là-bas, ce qui en fait des preuves pour l'audit.

> L'application « Demandes internes » est vulnérable par construction. Elle ne sort jamais de
> l'environnement de formation, et toutes ses données sont fictives.
