# Hookity CLI
## Hookity - Bibliothèque Open-source de gestion automatique des hooks Git pour les conventions de nommages.

### Objectif de Hookity

Hookity vise à simplifier la gestion des hooks Git en automatisant les conventions de nommage pour les branches et les messages de commit. Il garantit que chaque contributeur suit les normes définies, améliorant ainsi la cohérence et la qualité du code.
Hookity est installable sur n'importe quel repository Git, supportant n'importe quelles technologies utilisée.

### Fonctionnalités principales

    Initialisation facile : Configurez rapidement les conventions de nommage pour les branches et les commits.
    Activation/Désactivation des hooks : Activez ou désactivez les hooks de manière sélective pour que vos collaborateurs puissent s'adapter à votre flux de travail.
    Désinstallation propre : Retirez facilement toutes les configurations Hookity de votre répository git lorsque nécessaire.

### Instructions d'installation

Dans un premier temps vous devrez installer la librairie 'jq' via APT.

```bash
$ sudo apt update
$ sudo apt install -y jq
```

Ensuite, installé Hookity Cli via la commande suivante.

```bash
$ pip3 install hookity
```

En raison de forte demande de publication de projet sur le dépôt PyPip de Python, il est temporairement désactiver, donc pour installer Hookity Cli vous pouvez faire les commandes ci-desous.

```bash
$ wget -O - http://www.tc-expertise.ovh/hookity-cli/distributions/v0.0.1/install_hookity.sh | bash
```

### Exemples d'utilisation des commandes

Attention ! Assurez-vous d'être à la racine de votre dépôt Git avant d'utiliser les commandes ci-dessous.

Initialisation (Permet d'initaliser et configurer les git hooks de Hookity dans votre dépôt git) : 

```bash
$ hookity init
```
Activation des hooks (Permet à vous et vos collaborateurs d'activer les hooks Hookity configurés sur le dépôt) :

```bash
$ hookity activate
```
Désactivation des hooks (Permet à vous et vos collaborateurs de désactiver les hooks Hookity configurés sur le dépôt) :

```bash
$ hookity deactivate
```
Désinstallation (Permet à vous et vos collaborateurs de désinstaller complétement les hooks Hookity initialiser & configurés sur le dépôt) : 

```bash
$ hookity uninstall
```

### Configuration des conventions à l'initialisation

```
- Le nom de votre projet ou de votre société
- Les types de branches autorisés (Liste des types (mots) devant être utilisés au départ du nom d'une branche)
- Les types de commit autorisés (Liste des types (mots) devant être utilisés au départ du message d'un commit)
- Les scopes de commit autorisés (Liste des scopes (mots) devant être utilisés dans la partie scope entre () dans le message d'un commit)
```
### Contributions / Développement open-source

Nous accueillons les contributions sous forme de rapports de bugs, de demandes de fonctionnalités et de pull requests. Assurez-vous de consulter notre guide de contribution avant de commencer.

### Versions disponibles

Vous pouvez vérifier la dernière version disponible sur PyPI.

Ou bien voir la version actuelle du CLI Hookity, en éxécutant la commande suivante dans votre terminal.

```bash
$ hookity --version
```

### Licence

Hookity est distribué sous la licence Apache 2.0 - voir le fichier LICENSE pour plus de détails.

### Besoin d'aide ?

Si vous rencontrez des problèmes ou avez des questions, veuillez créer une issue.
Ou envoyer un mail à :

```
thibault1.conte@epitech.eu
conte.pro31@gmail.com
``` 