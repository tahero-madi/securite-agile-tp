# TP3-A — Protéger le dépôt, lancer le pipeline

**Jour 2, 09:55 · 30 min · par équipe.** Objectif : poser les protections qui rendent le pipeline
incontournable, puis le voir tourner. Support : sections 3.1 à 3.3 et 3.6.

**Avant tout (10 min, chacun) :** ouvrez votre VM, installez les outils, créez votre jeton d'accès et clonez
le projet : étapes 2 à 6 de [Avant de commencer](../avant-de-commencer.md). Prenez ensuite un instantané de
la VM.

## Étape 1 — Lire le pipeline

**Pourquoi.** Le pipeline exécute du code avec les droits de votre projet et ses secrets. Avant de lui faire
confiance, on le lit.

Ouvrez `.gitlab-ci.yml` (dans GitLab ou sur votre VM) et répondez en équipe :

1. Combien d'étapes (`stages`) ? Lesquelles ?
2. Quels jobs sont actifs aujourd'hui ? Que signifie le point devant les autres ?
3. Quelles images de conteneur sont utilisées ?
4. Pourquoi chaque outil est-il épinglé sur une version précise (`bandit==1.9.4`, `gitleaks:v8.26.0`) ?
   Une image n'est **pas** épinglée : laquelle, et quel est le risque ?

## Étape 2 — Protéger `main`

**Pourquoi.** Sans protection, n'importe quel membre peut pousser directement sur `main` et contourner la
revue comme le pipeline.

**Paramètres > Dépôt > Branches protégées** (Settings > Repository > Protected branches) :

- branche `main` ;
- **Autorisé à fusionner** (Allowed to merge) : Maintainers ;
- **Autorisé à pousser et fusionner** (Allowed to push and merge) : **Personne** (No one).

Puis vérifiez depuis votre VM :

```bash
cd ~/equipe-a                       # ou equipe-b
git switch main && git pull
echo "test" >> README.md && git commit -am "Test push direct"
git push origin main                # doit être refusé
git reset --hard origin/main        # annule le commit de test
```

Le message attendu : `You are not allowed to push code to protected branches on this project.`

## Étape 3 — « Le pipeline doit réussir »

**Pourquoi.** Sans cette option, un pipeline rouge n'empêche pas de fusionner : les contrôles ne seraient
que des avis.

**Paramètres > Merge requests** (Settings > Merge requests), section **Vérifications de fusion** (Merge
checks) : cochez **Le pipeline doit réussir** (Pipelines must succeed), puis **Enregistrer**.

## Étape 4 — La variable `SECRET_KEY`, masquée et protégée

**Pourquoi.** Un secret ne vit jamais dans le code : il vit dans une variable CI/CD, injectée au moment du
job. **Masquée**, sa valeur est remplacée par `[MASKED]` dans les journaux. **Protégée**, elle n'est
transmise qu'aux pipelines des branches protégées.

**Paramètres > CI/CD > Variables** (Settings > CI/CD > Variables), **Ajouter une variable** :

- **Clé :** `SECRET_KEY` ;
- **Valeur :** générez-la sur votre VM avec `python3 -c "import secrets; print(secrets.token_hex(32))"` ;
- **Visibilité :** Masquée (Masked) ; cochez **Protéger la variable** (Protect variable).

## Étape 5 — Une branche, une merge request, un pipeline vert

Depuis votre VM :

```bash
git switch -c securite/pipeline
echo "- Pipeline : tout passe par une merge request." >> README.md
git commit -am "Règle : passage obligatoire par une merge request"
git push -u origin securite/pipeline
```

Git affiche un lien pour créer la merge request : ouvrez-le, cible `main`, puis **Créer la merge request**.
Suivez le pipeline dans l'onglet **Pipelines** de la merge request : un seul job, `tests`, doit passer au
vert. **Ne fusionnez pas** : la branche resservira aux TP3-B et TP3-C.

## Point de contrôle

- Un push direct sur `main` est refusé.
- Le pipeline de la merge request est vert.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP3-B](../tp3b/README.md)
