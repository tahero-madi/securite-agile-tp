# Corrigé du TP4-C

## Une présentation qui convainc le comité

> « Nos trois risques principaux sont R-02 (connexion sans limite, critique), R-01 (CSRF, élevé) et R-04
> (nouvelle CVE après livraison, élevé). Les failles du TP3-C sont corrigées : voici la merge request, le
> pipeline vert avec ses quatre contrôles bloquants, et les huit tests de sécurité. Nous acceptons R-06, signé
> par notre Product Owner, réexamen à la prochaine version. Décision : **pas de mise en production tant que
> R-02 est ouvert** ; elle est prévue en fin de sprint 2, avec R-02 et R-01 traités. »

Ce qui fait la différence : **des preuves montrées**, un risque critique qui **bloque** la décision au lieu
d'être minimisé, et une date.

## Les questions que pose souvent le comité

| Question | Réponse attendue |
| --- | --- |
| « Pourquoi ne pas livrer maintenant et corriger ensuite ? » | Un risque critique ouvert (score 12) passe avant la mise en production : c'est la règle que l'équipe s'est donnée au TP2-C. Livrer l'exposerait réellement. |
| « Qui a accepté ce risque, et jusqu'à quand ? » | Le Product Owner, par écrit, avec une date de réexamen. Sans signature ni date, ce n'est pas une acceptation, c'est un oubli. |
| « Comment saurez-vous si une nouvelle faille apparaît après la livraison ? » | Pipeline nocturne sur les dépendances, SBOM suivi, veille CERT-FR, priorisation par KEV et EPSS (module 4). |
| « Combien cela coûte-t-il au sprint suivant ? » | La part de capacité réservée à la sécurité dans le plan de remédiation, en points. |

## La question du premier matin

**À quel moment du sprint ces failles auraient-elles dû être attrapées, et par qui ?**

| Faille de la démonstration | Où elle est attrapée désormais | Par qui |
| --- | --- | --- |
| Lecture de la demande d'un autre agent | Abuse case au backlog, menace M-01, critère de la story SEC-01, test dans le pipeline | Product Owner et champion sécurité à l'affinage ; Developers ; pipeline |
| Injection SQL | Story SEC-03, test, Bandit et Semgrep bloquants | Developers ; pipeline |
| XSS stockée | Story SEC-04, test, Semgrep bloquant | Developers ; pipeline |
| Clôture par un simple agent | Story SEC-02, test | Developers ; revue de la merge request |

Autrement dit : **au plus tôt**, dès le backlog et la Definition of Ready, et **par toute l'équipe**, avec le
pipeline comme filet de sécurité.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
