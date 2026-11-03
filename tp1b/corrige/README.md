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

Les abuse cases reprennent les trois attaques de la démonstration du matin : c'est voulu. Ce qu'on a vu
fonctionner contre l'application devient une exigence.

## Estimation et priorisation

- Les stories qui portent `donnees::sensibles` (consultation, recherche) méritent souvent un point de plus
  que leurs voisines : il faut un contrôle d'accès et un test.
- En MoSCoW, les deux abuse cases de contrôle d'accès sont des *Must* : la vision produit dit « sans exposer
  les données d'un agent à un autre ».

## Pièges fréquents

- **Un critère qui n'est pas testable** : « la recherche est sécurisée ». Un critère dit quoi saisir et quel
  résultat attendre.
- **Des abuse cases sans critère négatif.** « En tant qu'attaquant, je veux pirater l'application » ne dit
  pas ce que le système doit refuser.
- **Estimer seul.** Le planning poker n'a d'intérêt que si les écarts sont discutés.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
