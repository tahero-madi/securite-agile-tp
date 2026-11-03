# Corrigé du TP4-A

## Les constats attendus

Sur une application corrigée au TP3-C. Si votre équipe auditée n'a pas tout corrigé, les failles restantes
s'ajoutent à cette liste.

| Constat | Criticité suggérée | Recommandation |
| --- | --- | --- |
| Aucun jeton anti-CSRF sur les formulaires (clôture, création) | Élevée | Jeton CSRF (Flask-WTF) et test associé |
| Essais de mots de passe illimités, pas de double authentification pour les gestionnaires | Élevée | Limitation de débit, verrouillage temporisé, double authentification des gestionnaires |
| RIB stocké en clair dans une demande | Moyenne | Champ dédié chiffré, ou interdiction de saisie ; purge à la clôture |
| Image Docker en root, non épinglée (si non corrigée) | Moyenne | `python:3.12-slim` épinglée par empreinte, utilisateur dédié |
| Aucun scan planifié après la livraison | Moyenne | Pipeline nocturne (SCA), suivi du SBOM dans Dependency-Track |
| Relecture des merge requests non imposée | Moyenne | Règle d'approbation (édition payante), ou convention écrite dans la DoD et vérifiée |
| En-têtes de sécurité signalés par ZAP (si non corrigés) | Faible à moyenne | CSP, `X-Frame-Options`, `X-Content-Type-Options` |

## Ce que dit le rapport ZAP

- **Sur l'application vulnérable :** en-têtes absents (Content-Security-Policy, anti-clickjacking,
  `X-Content-Type-Options`), cookie de session sans `SameSite` ni `Secure`, et souvent les traces du mode
  debug.
- **Sur l'application corrigée :** l'essentiel de ces alertes disparaît. Restent en général des alertes
  informatives ou faibles : à trier comme au TP3-B, sans les ignorer d'office.
- **Ce que ZAP ne voit pas :** l'absence de jeton CSRF et le contrôle d'accès entre agents passent souvent
  inaperçus d'un scan passif sans compte. C'est la revue et l'audit qui les trouvent.

## Une grille bien remplie

- **Chaque note s'appuie sur un lien**, pas sur « l'équipe nous a dit que ».
- **La question 6** (relecture des merge requests) se vérifie dans l'onglet *Fusionnées* : qui a ouvert,
  qui a fusionné ? Si c'est toujours la même personne, la note est 0 ou 1, quelle que soit la DoD.
- **La question 11** (critères couverts par des tests) se vérifie dans `tests/test_securite.py` **et** dans
  le pipeline : un test qui existe mais qui est ignoré (`skip`) ne prouve rien.

---

[Énoncé](../README.md) · [Sommaire](../../README.md)
