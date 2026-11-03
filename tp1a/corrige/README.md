# Corrigé du TP1-A

## Ce qui doit exister à la fin

| Élément | Attendu |
| --- | --- |
| Labels | 10 labels : 3 `type::`, 3 `risque::`, `donnees::sensibles`, 3 `etat::` |
| Tableau | Open · `etat::a-faire` · `etat::en-cours` · `etat::en-revue` · Closed |
| Jalon | `Sprint 1`, deux semaines |
| README | Section « Équipe » (PO, Scrum Master, champion sécurité) et « Règles de fonctionnement » |

Déplacer un ticket d'une colonne à l'autre change son label `etat::` : le tableau et les labels restent
cohérents sans effort.

## La question à débattre

**En quoi `donnees::sensibles` aide-t-il le Product Owner ?** Il signale les stories qui manipulent des
données personnelles, bancaires ou confidentielles. Ces stories demandent plus de travail (critères de
sécurité, modélisation des menaces, plan de données au TP4-B), donc plus de points, et un défaut sur elles
coûte plus cher. Le label permet aussi de filtrer le backlog : « montre-moi tout ce qui touche des données
sensibles » avant une revue ou un audit.

## Pièges fréquents

- **Une limite de WIP purement décorative.** La règle doit être écrite et appliquée : si une troisième
  story entre en cours, l'équipe en termine une avant.
- **Des rôles flous.** Le champion sécurité n'est pas « celui qui fait la sécurité » : c'est un relais.
  La sécurité reste l'affaire de toute l'équipe.
- **La règle de relecture oubliée.** L'édition gratuite de GitLab n'impose pas d'approbation des merge
  requests : la règle « relue par une autre personne » n'existe que si l'équipe l'écrit et s'y tient. Elle
  reviendra dans la Definition of Done au TP1-C et dans l'audit au TP4-A.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
