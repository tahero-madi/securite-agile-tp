# TP3-B — Activer les contrôles, lire les rapports

**Jour 2, 10:25 · 45 min · par équipe, un ou deux outils chacun.** Objectif : brancher les contrôles de
sécurité automatisés, puis apprendre à lire et trier ce qu'ils trouvent. Support : sections 3.5 à 3.7.

## Étape 1 — Activer cinq contrôles en observation (10 min)

**Pourquoi.** On commence toujours en **observation** (`allow_failure: true`) : le contrôle produit son
rapport sans bloquer, ce qui permet de mesurer le bruit avant de décider d'un seuil.

Dans GitLab, **Compilation > Éditeur de pipeline** (Build > Pipeline editor), en choisissant la branche
**`securite/pipeline`** en haut de la page. Retirez le point devant ces cinq jobs :

| Avant | Après | Famille |
| --- | --- | --- |
| `.secrets-gitleaks:` | `secrets-gitleaks:` | Détection de secrets |
| `.sast-bandit:` | `sast-bandit:` | SAST, spécialisé Python |
| `.sast-semgrep:` | `sast-semgrep:` | SAST, règles de l'équipe |
| `.sca-pip-audit:` | `sca-pip-audit:` | Analyse des dépendances (SCA) |
| `.sbom-cyclonedx:` | `sbom-cyclonedx:` | Inventaire des composants (SBOM) |

Laissez `.dast-zap` et `.sast-sonarqube` cachés. L'éditeur valide la syntaxe : **Valider les modifications**
(Commit changes). Le pipeline de la merge request se relance ; les contrôles en défaut s'affichent en orange
(avertissement), pas en rouge.

Vous pouvez aussi faire la modification sur votre VM, puis `git pull` avant et `git push` après.

## Étape 2 — Récupérer les rapports (10 min)

Répartissez-vous les outils. Dans le pipeline, ouvrez chaque job : le **journal** montre le résultat lisible,
et le bouton **Parcourir** des **artefacts** du job donne le rapport complet (`rapports/*.json`).

**Question pour celui qui a Gitleaks :** le jeton trouvé est-il encore dans le code de la branche ? Où
Gitleaks l'a-t-il trouvé ? (indice : `GIT_DEPTH: "0"` dans le job.)

## Étape 3 — Le tableau de tri (20 min)

**Pourquoi.** Un rapport brut ne sert à rien. Chaque alerte doit être qualifiée : vraie ou fausse, grave ou
non, et reliée à une menace connue, pour finir en ticket ou en exception justifiée.

Créez dans votre projet le fichier `docs/tri-des-alertes.md` avec un tableau :

| Outil | Défaut | Fichier:ligne | Vrai / faux positif | Criticité | Menace (M-0x) |
| --- | --- | --- | --- | --- | --- |

Une ligne par alerte. Regroupez les alertes de même cause (le même défaut vu par deux outils).

## Étape 4 — La question à trancher (5 min)

**Quel outil a détecté M-01, la lecture de la demande d'un autre agent ?**

## Point de contrôle

Les cinq contrôles tournent en observation ; chaque défaut est trié et relié à une menace.

**Option**, si le formateur a mis un serveur SonarQube à disposition : activez aussi `sast-sonarqube`, avec
les variables masquées `SONAR_HOST_URL` et `SONAR_TOKEN`, et comparez ses résultats à ceux de Semgrep.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP3-C](../tp3c/README.md)
