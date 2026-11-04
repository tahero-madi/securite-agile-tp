# Corrigé du TP1-B

## Exemples de stories et d'abuse cases attendus

| Type | Story | Critère d'acceptation clé |
| --- | --- | --- |
| Story | En tant qu'agent, je veux créer une demande avec un titre et une description, afin de la soumettre au service. | Titre obligatoire, 200 caractères maximum |
| Story | En tant qu'agent, je veux rechercher mes demandes par titre, afin de les retrouver vite. | Seules mes demandes apparaissent |
| Story | En tant qu'agent, je veux consulter le détail et le statut de ma demande. | Je vois titre, description et statut |
| Story | En tant que gestionnaire, je veux voir toutes les demandes ouvertes. | Toutes les demandes de tous les agents apparaissent |
| Story | En tant que gestionnaire, je veux clôturer une demande traitée. | Le statut passe à « clôturée » |
| Abuse case | En tant qu'agent malveillant, je veux lire la demande d'un collègue en changeant son numéro dans l'URL, afin de lire ses données. | La demande d'un autre agent renvoie une erreur 404 |
| Abuse case | En tant qu'agent malveillant, je veux clôturer les demandes des autres. | Un agent reçoit une erreur 403 sur la clôture |
| Abuse case | En tant qu'attaquant, je veux injecter du code dans la recherche pour extraire la base. | Une saisie `' OR 1=1 --` ne renvoie que mes demandes |
| Abuse case | En tant qu'attaquant, je veux glisser un script dans une description pour qu'il s'exécute chez le gestionnaire. | Le texte `<script>` s'affiche tel quel, sans s'exécuter |
| Story | En tant qu'utilisateur, je veux me connecter avec mon identifiant et mon mot de passe, afin d'accéder à mes demandes. | Bon couple → accès, mauvais → erreur ; mot de passe stocké en empreinte forte (pas MD5) et absent des journaux |
| Story | En tant qu'agent, je veux modifier ma demande tant qu'elle est ouverte, afin de corriger une erreur. | Seul le propriétaire modifie ; une demande clôturée n'est plus modifiable |
| Story | En tant que gestionnaire, je veux rechercher parmi toutes les demandes par mot-clé, afin de traiter les urgentes d'abord. | La recherche couvre toutes les demandes ; une saisie piégée ne renvoie que des résultats légitimes |
| Abuse case | En tant qu'attaquant, je veux essayer des milliers de mots de passe sur la connexion, afin d'ouvrir un compte gestionnaire. | Après N tentatives échouées, la connexion est temporisée ou bloquée (6ᵉ essai refusé) |
| Abuse case | En tant qu'attaquant ayant accès aux journaux, je veux y lire des mots de passe en clair. | Après une connexion réussie ou échouée, aucun mot de passe n'apparaît dans les logs |

Les abuse cases reprennent les trois attaques de la démonstration du matin : c'est voulu. Ce qu'on a vu
fonctionner contre l'application devient une exigence.

## Estimation et priorisation

Chaque ticket — stories **et** abuse cases — est estimé en planning poker (suite `1, 2, 3, 5, 8, 13`) et
classé en MoSCoW par le Product Owner. Exemple de backlog complet, estimé et priorisé :

| Ticket | Points | MoSCoW |
| --- | --- | --- |
| Créer une demande | 2 | Must |
| Consulter le détail et le statut de ma demande | 2 | Must |
| Gestionnaire : voir toutes les demandes ouvertes | 3 | Must |
| Gestionnaire : clôturer une demande | 2 | Must |
| Se connecter (stockage et journalisation sûrs du mot de passe) | 5 | Must |
| Rechercher mes demandes par titre | 3 | Should |
| Modifier ma demande tant qu'elle est ouverte | 3 | Should |
| Gestionnaire : rechercher / filtrer toutes les demandes | 3 | Could |
| Abuse : lire la demande d'un autre (IDOR) → 404 | 3 | Must |
| Abuse : clôturer la demande d'un autre → 403 | 3 | Must |
| Abuse : injection SQL dans la recherche | 3 | Must |
| Abuse : XSS stockée dans une description | 2 | Must |
| Abuse : mot de passe lisible dans les journaux | 2 | Must |
| Abuse : force brute sur la connexion | 5 | Should (débattu) |

**Comment lire ce tableau.**

- **Points ≠ priorité.** Les points mesurent l'effort (échelle à écarts croissants) ; le MoSCoW mesure
  l'importance. « Se connecter » coûte 5 points *et* reste un *Must* : cher ne veut pas dire optionnel.
- **Les `donnees::sensibles` prennent souvent un point de plus** (consultation, recherche, connexion) : il
  faut y ajouter un contrôle d'accès et un test.
- **Must.** Le cœur fonctionnel (déposer, suivre, traiter, clôturer) et les défenses non négociables :
  contrôle d'accès (IDOR, clôture), injection, XSS, stockage et journalisation du mot de passe. La vision
  produit — « sans exposer les données d'un agent à un autre » — rend ces abuse cases obligatoires.
- **Should / Could.** Les conforts : recherche de ses propres demandes, modification, filtre du gestionnaire
  (qui voit déjà tout). Ce sont les premiers sacrifiés si la capacité du sprint est atteinte.
- **Le cas à débattre : la force brute.** Risque élevé (R-02 au TP4) mais coûteux (5). Beaucoup d'équipes le
  passeront en *Must* : c'est l'arbitrage type où le champion sécurité pousse et où le PO tranche. Laissez la
  discussion avoir lieu plutôt que d'imposer la réponse.
- **Un exemple de *Won't* (this time) :** exporter les demandes en PDF, ou les notifier par e-mail — utiles
  un jour, hors périmètre de ce sprint. L'écrire en *Won't* évite d'y revenir sans cesse.

## Pièges fréquents

- **Un critère qui n'est pas testable** : « la recherche est sécurisée ». Un critère dit quoi saisir et quel
  résultat attendre.
- **Des abuse cases sans critère négatif.** « En tant qu'attaquant, je veux pirater l'application » ne dit
  pas ce que le système doit refuser.
- **Estimer seul.** Le planning poker n'a d'intérêt que si les écarts sont discutés.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
