# Avant de commencer

Trois choses à préparer : votre compte GitLab (dès le TP1-A), puis votre VM et votre jeton d'accès
(au début du TP3-A, premier TP qui touche au code).

## 1. Votre compte GitLab

1. Ouvrez https://gitlab-3033.mooo.com dans le navigateur de votre poste.
2. Connectez-vous avec l'identifiant et le mot de passe initial que le formateur vous a remis. GitLab vous
   demande aussitôt d'en choisir un nouveau.
3. **Recommandé :** activez la double authentification. Avatar en haut à gauche, **Modifier le profil**,
   puis **Compte** (Account) et **Activer l'authentification à deux facteurs**. Scannez le QR code avec une
   application d'authentification (Google Authenticator, Microsoft Authenticator, FreeOTP…) et
   **conservez les codes de récupération**.
4. **Facultatif :** l'interface est en anglais par défaut. Pour la passer en français : **Préférences**,
   section **Localisation**, langue **Français**. Les énoncés donnent les deux noms des menus.

**Trouver votre projet.** Ouvrez directement https://gitlab-3033.mooo.com/formation-3033, ou, dans la page
**Projets**, l'onglet **Membre** (l'onglet par défaut, « Contribué », reste vide tant que vous n'avez rien
poussé).

| Projet | Votre rôle |
| --- | --- |
| Celui de votre équipe | Maintainer : vous administrez le projet |
| Celui de l'autre équipe | Reporter : lecture seule, pour l'audit du TP4-A |

## 2. Votre VM

Le formateur vous indique le nom de votre VM (`lab-apprenant-01` à `lab-apprenant-06`), son adresse et
vos identifiants de connexion. Connectez-vous depuis votre poste :

```bash
ssh stagiaire@ADRESSE-DE-VOTRE-VM
```

Avec VS Code : extension **Remote - SSH**, puis **Connect to Host** avec la même adresse. Vous éditez alors
les fichiers de la VM comme s'ils étaient sur votre poste.

## 3. Votre jeton d'accès personnel

**Pourquoi.** Pour cloner et pousser en HTTPS, Git a besoin d'un secret. Un jeton d'accès vaut mieux que
votre mot de passe : il est limité à certaines actions, il expire, et il se révoque sans toucher à votre
compte. Si vous avez activé la double authentification, il est même obligatoire.

Dans GitLab : avatar, **Modifier le profil**, **Jetons d'accès** (Access tokens), **Ajouter un jeton** :

- **Nom :** `vm-formation` ;
- **Date d'expiration :** le lendemain de la formation ;
- **Portées :** `read_repository` et `write_repository`, rien d'autre.

Copiez le jeton affiché : GitLab ne le montrera plus. Ne le collez nulle part ailleurs que dans Git.

## 4. Configurer Git et cloner le projet

Sur votre VM (remplacez `equipe-a` par le projet de votre équipe) :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "prenom.nom@exemple.fr"
git config --global credential.helper "cache --timeout=28800"

git clone https://gitlab-3033.mooo.com/formation-3033/equipe-a.git
# Username : votre identifiant GitLab ; Password : votre jeton
cd equipe-a
```

**Ligne par ligne.**

- `user.name` et `user.email` : signent vos commits ; ils apparaîtront dans l'historique du projet.
- `credential.helper "cache --timeout=28800"` : garde le jeton **en mémoire** pendant 8 heures. Évitez
  `credential.helper store`, qui l'écrirait en clair dans `~/.git-credentials` : c'est le genre de secret
  qui finit dans une sauvegarde ou une capture d'écran.
- `git clone` : récupère le projet **avec tout son historique**. Retenez-le pour le TP3-B.

## 5. Lancer les tests et l'application

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest                    # 6 tests verts, 1 ignoré
flask --app app init-db
flask --app app run                 # écoute sur 127.0.0.1:5000
```

L'application n'écoute que sur la VM elle-même. Pour l'ouvrir dans le navigateur de votre poste, créez un
tunnel SSH depuis **votre poste**, dans un second terminal :

```bash
ssh -L 5000:127.0.0.1:5000 stagiaire@ADRESSE-DE-VOTRE-VM
```

Puis ouvrez http://localhost:5000. Comptes de démonstration : `alice` / `alice2026` et `bob` / `bob2026`
(agents), `gestion` / `gestion2026` (gestionnaire).

## Trois règles

1. **Tout est fictif** : comptes, demandes, RIB, jetons. N'utilisez jamais de vraies données, même pour un
   test rapide.
2. **L'application est vulnérable** : laissez-la écouter sur `127.0.0.1`, ne l'exposez pas sur Internet.
3. **Les scans ne visent que l'application de la formation**, jamais un autre site ou serveur.

---

[Sommaire](README.md) · [En cas de blocage](en-cas-de-blocage.md)
