#!/bin/bash

commit_message=$(cat .git/COMMIT_EDITMSG)

if ! [[ $commit_message =~ ^(build|docs|feat|fix|perf|refactor|test)(\([a-z]+\))?+[^:]+:[[:space:]]+.*$ ]]; then
    echo -e """
    \e[1;33mVotre message de commit actuel : '"$commit_message"'\033[0m

    \033[1;31mErreur : Nommage de votre commit non conforme !\033[0m
    \033[1;34mInformation : Votre message de commit ne suit pas la convention PARK-IT.\033[0m
    
    \033[4;1mFormat Attendu\033[0m : \033[1;32mCOMMIT_TYPE(COMMIT_SCOPE) : <COMMIT_SHORT_DESCR>\033[0m
    
    \033[4;1mTypes de commit disponibles\033[0m :
    \033[1;32m- build
    - docs
    - feat
    - fix
    - perf
    - refactor
    - test\033[0m

    \033[4;1mScope de commit correct\033[0m :

    \e[1;37mFaites comme vous souhaitez, déduisez par logique et soyez cohérents, faites en fonction du service, de l'outil,
    du pôle, etc... Sur lequel vous travaillez.\033[0m
    \e[1;33mSuivez les exemples ci-dessous pour l'inspiration et la logique\033[0m 

    \033[4;1mExemple de message correct\033[0m : 
    
    \033[1;32m- feat(authentification-service) : Implémentation du service d'authentification utilisateur via JWT\033[0m
    \033[1;32m- feat(devops-ansible) : Implémentation d'un playbook d'installation de python vers machines distantes\033[0m
    \033[1;32m- fix(authentification-service) : Correction du service d'authentification utilisateur via JWT encoder HS\033[0m
    \033[1;32m- refactor(authentification-service) : Optimisation et refonte du code du service d'authentification.\033[0m
    \033[1;32m- docs(authentification-service) : Création du README du service d'authentification.\033[0m
    \033[1;32m- build(application-parkit) : Build de l'apk test RELEASE de l'application parkit avec mapbox SDK\033[0m
    \033[1;32m- test(application-parkit) : Ajout du test pour le click du boutton 'Se connecter' + code coverage\033[0m
    """
    exit 1
fi

exit 0