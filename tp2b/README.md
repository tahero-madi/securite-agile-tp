# TP2-B — Écrire les security user stories

**Jour 1, 14:40 · 40 min · par équipe.** Objectif : transformer vos menaces en stories de sécurité dont
chaque critère pourra devenir un test automatisé. Support : sections 2.4 et 2.8. Modèle :
`docs/modeles/01-user-story-securite.md`.

## Étape 1 — Une story par menace (20 min)

**Pourquoi.** Une menace qui n'entre pas dans le backlog ne sera jamais traitée : elle n'a ni priorité, ni
estimation, ni responsable. La story de sécurité la fait entrer dans le flux normal de l'équipe.

À partir de vos 5 premières menaces, créez **4 à 6 tickets** avec le label `type::securite`, numérotés
`SEC-01`, `SEC-02`… dans le titre. Copiez la structure du modèle dans la description. Chaque story cite :

- **sa menace** (`M-0x`) et **sa catégorie OWASP Top 10:2025** (`A01`, `A05`…) ;
- un **scénario autorisé** : ce qui doit continuer de marcher ;
- un **scénario d'abus** : ce qui doit être refusé.

## Étape 2 — Des critères au format Étant donné / Quand / Alors (15 min)

**Pourquoi.** Ce format (Gherkin) oblige à préciser l'état de départ, l'action et le résultat attendu.
Écrit ainsi, un critère se traduit presque mot pour mot en test au TP3-C.

```gherkin
Scénario : un agent ne lit pas la demande d'un autre agent
  Étant donné que bob est connecté
  Quand il ouvre la demande n° 1, qui appartient à alice
  Alors il reçoit une erreur 404
```

Rappel des comptes de l'application : `alice` (agent, demandes 1 et 2), `bob` (agent, demandes 3 et 4),
`gestion` (gestionnaire).

Ajoutez à chaque story le label `risque::` correspondant au score de sa menace, et `donnees::sensibles`
si elle protège une donnée sensible.

## Étape 3 — Relecture croisée (5 min)

Échangez une story avec l'autre équipe. Question unique : **peut-on écrire le test à partir de ce critère,
sans rien demander à son auteur ?** Si non, reformulez.

## Point de contrôle

Chaque critère peut devenir un test : on sait quoi saisir et quel résultat attendre.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP2-C](../tp2c/README.md)
