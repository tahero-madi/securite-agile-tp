# Corrigé du TP4-B

## Le registre indicatif

| ID | Risque (cause → événement → conséquence) | V | I | Score | Traitement | Mesure |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | L'absence de jeton anti-CSRF permet à un site tiers de faire clôturer une demande par un gestionnaire connecté, ce qui fausse le suivi | 3 | 3 | 9 | Réduire | Jeton CSRF ; `SameSite` déjà posé |
| R-02 | Les essais illimités permettent de deviner le mot de passe d'un gestionnaire, qui peut alors tout lire et tout clôturer | 3 | 4 | 12 | Réduire | Limitation de débit, double authentification |
| R-03 | Un RIB en clair fuit par une sauvegarde ou un export | 2 | 4 | 8 | Réduire | Chiffrement du champ, purge à la clôture |
| R-04 | Une nouvelle CVE critique sur Werkzeug est publiée après la livraison et reste ignorée | 3 | 3 | 9 | Réduire | Pipeline nocturne, délai de 7 jours pour les critiques |
| R-05 | Une dépendance compromise du pipeline vole les variables CI/CD | 2 | 4 | 8 | Réduire | Images épinglées par empreinte, variables protégées |
| R-06 | Des erreurs détaillées s'affichent en production | 1 | 2 | 2 | Accepter | Debug piloté par variable, contrôlé en revue |

R-02 est **critique** (12) : il passe avant toute mise en production. R-06 est faible et déjà maîtrisé : son
acceptation est légitime, **à condition d'être signée par le Product Owner et datée**.

## Le plan des données sensibles indicatif

| Donnée | Classification | Où elle passe | Mesures | Conservation |
| --- | --- | --- | --- | --- |
| Mot de passe | Secret | Saisie, base (empreinte), **journaux** (avant correction) | scrypt, jamais journalisé, HTTPS | Tant que le compte existe |
| RIB dans une demande | Personnelle, financière | Saisie, base, sauvegardes, exports, **captures d'écran de tickets** | Champ dédié chiffré ou interdiction de saisie ; masquage à l'affichage ; purge | Jusqu'à la clôture, puis purge |
| Identité de l'agent | Personnelle | Base, journaux, tickets | Accès au plus juste ; identifiant plutôt que nom dans les journaux | Durée de l'emploi |
| Jetons et `SECRET_KEY` | Secret technique | Variables CI/CD, environnement d'exécution | Variables masquées et protégées ; rotation après fuite | Rotation régulière |
| Données de test | Fictives | Dépôt, pipeline | **Jamais de copie de production** | — |

## Le plan de remédiation indicatif

Capacité 20 points, dont **40 % réservés à la sécurité** au sprint 2, parce qu'un risque critique est
ouvert.

| Priorité | Action | Risque | Points | Preuve de clôture |
| --- | --- | --- | --- | --- |
| 1 | Limiter les essais de connexion ; double authentification des gestionnaires | R-02 | 5 | Test : 6e essai refusé ; capture du réglage |
| 2 | Jeton CSRF sur tous les formulaires | R-01 | 3 | Test : POST sans jeton refusé |
| 3 | Pipeline nocturne SCA | R-04 | 1 | Planification visible, premier rapport |
| 4 | Épingler les images par empreinte | R-05 | 1 | `.gitlab-ci.yml` relu en merge request |

**Risque accepté :** R-06, signé par le Product Owner, réexamen à la prochaine version.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
