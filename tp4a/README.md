# TP4-A — Audit croisé

**Jour 2, 14:00 · 45 min. L'équipe A audite le projet de l'équipe B, et inversement.** Objectif : vérifier,
preuves à l'appui, que les pratiques de sécurité de l'autre équipe tiennent. Support : section 4.6. Modèle :
`docs/modeles/04-grille-audit-agile.md`.

Vous avez le rôle **Reporter** sur le projet de l'autre équipe : vous lisez tout (code, tickets, merge
requests, pipelines, rapports), vous ne modifiez rien.

**Préparation.** Dans **votre** projet, créez `docs/audit-equipe-b.md` (ou `audit-equipe-a.md`) en y copiant
la grille du modèle 04.

## Étape 1 — La grille d'audit (25 min)

**Pourquoi.** Un audit agile ne croit que ce qu'il voit. Chaque note s'appuie sur une preuve dans les outils
de l'équipe ; **ce qui n'est pas prouvé est noté 0**, même si l'équipe affirme le faire.

Notez les 16 questions de 0 à 3 :

| Note | Signification |
| --- | --- |
| 0 | Absent, ou non prouvé |
| 1 | Initié |
| 2 | En place (preuve exigée) |
| 3 | En place et prouvé dans la durée (preuve exigée) |

Pour chaque note de 2 ou 3, collez le **lien** vers la preuve : le ticket, la merge request, le job, le
fichier. Où chercher :

| Preuve | Où dans GitLab |
| --- | --- |
| Rôles, DoR, DoD | `README.md` du projet |
| Backlog, labels | **Planifier > Tableaux des tickets**, **Planifier > Éléments de travail** (Work items) |
| Modèle de menaces | `docs/` |
| Relecture des merge requests | **Code > Merge requests**, onglet **Fusionnées** (Merged) |
| Pipeline, seuils | `.gitlab-ci.yml`, **Compilation > Pipelines** |
| Rapports | Artefacts des jobs |

## Étape 2 — Scan OWASP ZAP (10 min)

**Pourquoi.** Les scanners du TP3-B lisent le code ; ZAP regarde l'application **en fonctionnement**, comme
un navigateur : en-têtes, cookies, réponses d'erreur.

L'équipe **auditée** active le job `dast-zap` : dans son `.gitlab-ci.yml`, sur une branche avec merge
request, elle retire le point devant `.dast-zap`. Le job lance l'application dans le conteneur, puis la
scanne en **mode passif** (*baseline*) : ZAP observe les réponses, il n'attaque rien.

Les **auditeurs** ouvrent ensuite le rapport `zap.html` dans les artefacts du job. Si le job ne fonctionne
pas, le formateur lance le scan sur une copie du projet audité et vous transmet le rapport.

> Un scan ne vise jamais une cible qui n'est pas explicitement autorisée : ici, uniquement l'application de
> la formation.

## Étape 3 — Les constats (10 min)

Rédigez **4 à 6 constats** dans le tableau du modèle : constat, preuve, criticité (critique, élevée,
moyenne, faible), recommandation, échéance proposée.

Remettez-les à l'équipe auditée sous forme de **tickets dans son projet** (un Reporter peut créer des
tickets), label `type::securite`, titre commençant par `AUDIT-`.

## Point de contrôle

- La grille est notée, avec un lien de preuve pour chaque note de 2 ou plus.
- Les constats sont remis à l'équipe auditée.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP4-B](../tp4b/README.md)
