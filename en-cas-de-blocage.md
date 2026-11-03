# En cas de blocage

| Symptôme | Cause probable | Solution |
| --- | --- | --- |
| La page **Projets** de GitLab est vide | L'onglet par défaut, « Contribué », ne liste que les projets où vous avez déjà poussé | Onglet **Membre**, ou https://gitlab-3033.mooo.com/formation-3033 |
| `git clone` ou `git push` : « HTTP Basic: Access denied » | Mot de passe du compte refusé (double authentification active), ou jeton mal copié, expiré, sans la bonne portée | Créez un nouveau jeton avec `read_repository` et `write_repository` ([Avant de commencer](avant-de-commencer.md#3-votre-jeton-daccès-personnel)), puis `git credential-cache exit` pour oublier l'ancien |
| `git push` refusé sur `main` : « You are not allowed to push code to protected branches » | Branche protégée au TP3-A : c'est voulu | Travaillez sur une branche et passez par une merge request |
| Le bouton **Merge** est grisé | « Le pipeline doit réussir » est activé et le pipeline est rouge ou en cours | Corrigez jusqu'au vert : c'est le but du TP3-C |
| Pipeline bloqué « en attente » (pending) | Les deux équipes lancent leurs pipelines en même temps : deux jobs tournent à la fois au plus | Patientez quelques minutes. Au-delà de 10 minutes, prévenez le formateur |
| Job en échec dès la première ligne, erreur YAML | Indentation cassée dans `.gitlab-ci.yml` | **Build > Pipeline editor** (Compilation > Éditeur de pipeline) signale la ligne fautive avant de valider |
| Variable CI/CD vide dans un job | Une variable **protégée** n'existe que sur les branches protégées | C'est le comportement attendu sur une branche de travail ; décochez « Protéger » seulement pour un essai |
| Job `secrets-gitleaks` toujours rouge après avoir supprimé le jeton du code | Gitleaks lit tout l'historique : le jeton y est toujours | C'est la leçon du TP3-C : voir son [corrigé](tp3c/corrige/README.md) |
| `pip install` très lent ou en échec sur la VM | Réseau ou miroir PyPI | Relancez ; si cela persiste, prévenez le formateur |
| http://localhost:5000 ne répond pas | Tunnel SSH absent, ou application arrêtée sur la VM | Relancez `flask --app app run` sur la VM et le tunnel `ssh -L 5000:127.0.0.1:5000 …` depuis votre poste |
| `flask: command not found` | Environnement virtuel non activé | `. .venv/bin/activate` dans le dossier du projet |
| Perte du téléphone de double authentification | — | Utilisez un code de récupération, ou demandez au formateur de réinitialiser votre double authentification |

Toujours bloqué ? Notez la commande, le message d'erreur exact et l'URL de la page, puis appelez le
formateur.

---

[Sommaire](README.md)
