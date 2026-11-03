# Corrigé du TP2-B

## Les stories attendues

| ID | Story | Scénario d'abus (critère testable) |
| --- | --- | --- |
| SEC-01 | En tant qu'agent, je veux que mes demandes ne soient visibles que par moi et les gestionnaires, afin de protéger leur contenu (M-01, A01). | Étant donné bob connecté, quand il ouvre `/demandes/1` qui appartient à alice, alors il reçoit une erreur 404. |
| SEC-02 | En tant que gestionnaire, je veux être le seul à pouvoir clôturer une demande (M-03, A01). | Étant donné alice connectée, quand elle envoie la clôture de la demande 1, alors elle reçoit une erreur 403 et le statut reste « ouverte ». |
| SEC-03 | En tant qu'agent, je veux que la recherche ne puisse pas lire d'autres données que les miennes (M-02, A05). | Étant donné alice connectée, quand elle recherche `' OR 1=1 --`, alors aucune demande de bob n'apparaît. |
| SEC-04 | En tant que gestionnaire, je veux que le texte des demandes s'affiche sans être interprété (M-04, A05). | Étant donné une description `<script>alert(1)</script>`, quand j'ouvre la demande, alors le texte s'affiche échappé. |
| SEC-05 | En tant que RSSI, je veux que les mots de passe soient hachés avec un algorithme adapté et absents des journaux (M-05, M-07, A04, A09). | Quand une connexion échoue, alors le journal contient l'identifiant mais pas le mot de passe ; l'empreinte stockée commence par `scrypt:` ou `pbkdf2:`. |
| SEC-06 | En tant qu'équipe, nous voulons qu'aucun secret ne soit dans le dépôt (M-06, A02). | Quand le pipeline s'exécute, alors Gitleaks ne détecte aucun secret non révoqué. |

## Exemple complet : SEC-01

```markdown
**ID :** SEC-01  **Lien menace :** M-01  **Référence :** OWASP Top 10:2025 A01 / ASVS 5.0 V8 (autorisation)

**En tant qu'**agent
**je veux** que mes demandes ne soient visibles que par moi et les gestionnaires
**afin de** protéger leur contenu, dont mes coordonnées bancaires
```

```gherkin
Scénario : un agent consulte sa propre demande
  Étant donné qu'alice est connectée
  Quand elle ouvre la demande n° 1, qui lui appartient
  Alors la demande s'affiche

Scénario : un agent ne lit pas la demande d'un autre agent
  Étant donné que bob est connecté
  Quand il ouvre la demande n° 1, qui appartient à alice
  Alors il reçoit une erreur 404
```

**Preuve attendue :** `tests/test_securite.py::test_un_agent_ne_voit_pas_la_demande_d_un_autre_agent` vert
dans le pipeline. Labels : `type::securite`, `risque::eleve`, `donnees::sensibles`.

## Pourquoi 404 et pas 403 ?

Un 403 dit « cette demande existe, mais elle n'est pas pour vous ». Un 404 ne confirme même pas son
existence : l'attaquant ne peut pas énumérer les numéros valides. Pour la clôture (SEC-02), le 403 convient :
c'est l'action qui est interdite au rôle, pas l'objet qui est caché.

## À retenir

Ces scénarios deviennent les tests automatisés du TP3-C, **mot pour mot**. C'est le fil qui relie la
conception du jour 1 au pipeline du jour 2.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
