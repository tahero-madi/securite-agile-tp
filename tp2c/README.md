# TP2-C — Re-prioriser et préparer la validation

**Jour 1, 15:20 · 25 min · mené par le Product Owner.** Objectif : faire entrer les stories de sécurité dans
l'ordre du backlog et décider, pour chacune, comment on prouvera qu'elle est faite. Support : sections 1.6
et 2.5.

## Étape 1 — Réordonner le backlog (10 min)

**Pourquoi.** Une story de sécurité laissée en bas du backlog n'est jamais faite. Le risque doit peser dans
l'ordre, au même titre que la valeur métier.

Le Product Owner réordonne la colonne `etat::a-faire` du tableau en croisant **valeur métier** et **score de
risque**, avec une règle :

> Une menace cotée **12 ou plus** (critique) passe avant toute nouvelle fonctionnalité.

## Étape 2 — Choisir la preuve de chaque story (10 min)

**Pourquoi.** Une story de sécurité « faite » sans preuve ne résistera pas à un audit (TP4-A). Choisir la
preuve maintenant, c'est savoir dès le départ ce que le sprint doit produire.

Pour chaque ticket `type::securite`, ajoutez dans la description une ligne :

```text
Preuve de clôture : <test automatisé | contrôle du pipeline | revue de code | test manuel> — <lequel>
```

Préférez le **test automatisé** chaque fois que c'est possible : il est rejoué à chaque modification et
empêche la faille de revenir.

## Étape 3 — Mettre à jour le jalon Sprint 1 (5 min)

Rattachez au jalon les stories de sécurité critiques. Si la capacité de 20 points est dépassée, le Product
Owner retire des stories fonctionnelles, pas l'inverse.

## Point de contrôle

SEC-01 à SEC-03 en tête du backlog, chacune avec sa preuve de clôture.

---

[Corrigé](corrige/README.md) · [Sommaire](../README.md) · TP suivant : [TP3-A](../tp3a/README.md)
