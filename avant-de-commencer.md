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

Pour les TP du jour 1, le navigateur de votre poste suffit : tout se passe dans GitLab.

## 2. Votre VM

Chaque participant a un **lien personnel** vers son environnement Hexceos. Ouvrez le vôtre (tableau
ci-dessous) dans le navigateur de votre poste : ni compte ni mot de passe à saisir.

| Participant | Nom | Équipe | Lien d'accès personnel |
| --- | --- | --- | --- |
| 01 | Thibault | A | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb9ckwxzckp |
| 02 | Rabeb | A | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb9p2zaeumc |
| 03 | Ilyes | A | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb94pwrwec4 |
| 04 | Stéphane | B | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb94yzby5w3 |
| 05 | Léo | B | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb9tmefkwm5 |
| 06 | Vincent | B | https://hra-ng.hexceos.cloud/p/37e8ccd3-5f2c-473b-8b24-a8a8f2ba9bb99vvz4qks |

> Ces environnements sont créés pour la durée de la formation puis supprimés. N'y mettez aucune donnée réelle.

1. Double-cliquez sur votre machine pour ouvrir sa console. Préférez le mode **Bureau distant** : la
   résolution s'adapte à votre écran. Le bouton **Plein écran** vous donne toute la place.
2. Si un mot de passe vous est demandé, il est sous l'icône **clé** (identifiants de la machine).
3. Le presse-papiers fonctionne dans les deux sens : bouton **Coller** de la barre d'outils.

**Prenez un instantané** (icône appareil photo) avant chaque TP qui modifie la machine : en cas d'erreur,
vous revenez à cet état en quelques secondes.

**À partir du TP3-A, travaillez dans la VM** : ouvrez GitLab dans le Firefox de la VM, codez dans VS Code
sur la VM, lancez l'application sur la VM.

## 3. Installer les outils (5 minutes, une seule fois)

Dans la VM, ouvrez un **Terminal** et lancez :

```bash
sudo apt-get update
sudo apt-get install -y git python3-venv
sudo snap install code --classic
```

- `git` et `python3-venv` ne sont pas installés par défaut sur Ubuntu Desktop.
- `code` est VS Code. Il apparaît ensuite dans le menu des applications, ou se lance par `code .` dans un
  dossier.

## 4. Votre jeton d'accès personnel

**Pourquoi.** Pour cloner et pousser en HTTPS, Git a besoin d'un secret. Un jeton d'accès vaut mieux que
votre mot de passe : il est limité à certaines actions, il expire, et il se révoque sans toucher à votre
compte. Si vous avez activé la double authentification, il est même obligatoire.

**Créez-le dans le Firefox de la VM**, pas sur votre poste : le secret ne quitte ainsi jamais la machine
qui s'en sert. Dans GitLab : avatar, **Modifier le profil**, **Jetons d'accès** (Access tokens),
**Ajouter un jeton** :

- **Nom :** `vm-formation` ;
- **Date d'expiration :** le lendemain de la formation ;
- **Portées :** `read_repository` et `write_repository`, rien d'autre.

Copiez le jeton affiché : GitLab ne le montrera plus. Ne le collez nulle part ailleurs que dans Git.

## 5. Configurer Git et cloner le projet

Dans le terminal de la VM (remplacez `equipe-a` par le projet de votre équipe) :

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "prenom.nom@exemple.fr"
git config --global credential.helper "cache --timeout=28800"

cd ~
git clone https://gitlab-3033.mooo.com/formation-3033/equipe-a.git
# Username : votre identifiant GitLab ; Password : votre jeton
cd equipe-a
code .                              # ouvre le projet dans VS Code
```

**Ligne par ligne.**

- `user.name` et `user.email` : signent vos commits ; ils apparaîtront dans l'historique du projet.
- `credential.helper "cache --timeout=28800"` : garde le jeton **en mémoire** pendant 8 heures. Évitez
  `credential.helper store`, qui l'écrirait en clair dans `~/.git-credentials` : c'est le genre de secret
  qui finit dans une sauvegarde ou une capture d'écran.
- `git clone` : récupère le projet **avec tout son historique**. Retenez-le pour le TP3-B.

## 6. Lancer les tests et l'application

Dans le terminal de la VM, depuis le dossier du projet :

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest                    # 6 tests verts, 1 ignoré
flask --app app init-db
flask --app app run                 # écoute sur 127.0.0.1:5000
```

Ouvrez **http://127.0.0.1:5000 dans le Firefox de la VM**. Comptes de démonstration : `alice` / `alice2026`
et `bob` / `bob2026` (agents), `gestion` / `gestion2026` (gestionnaire). `Ctrl+C` dans le terminal arrête
l'application.

L'application n'écoute que sur la VM elle-même : personne d'autre ne peut l'atteindre, et c'est voulu.

## Trois règles

1. **Tout est fictif** : comptes, demandes, RIB, jetons. N'utilisez jamais de vraies données, même pour un
   test rapide.
2. **L'application est vulnérable** : laissez-la écouter sur `127.0.0.1`, ne l'exposez pas sur le réseau.
3. **Les scans ne visent que l'application de la formation**, jamais un autre site ou serveur.

---

[Sommaire](README.md) · [En cas de blocage](en-cas-de-blocage.md)
