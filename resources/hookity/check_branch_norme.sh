#!/bin/bash

branch_name=$(git symbolic-ref HEAD --short 2>/dev/null)

if [[ $branch_name == "develop" || $branch_name == "main" ]]; then
    echo "Validation de convention ignorée pour les branches 'develop' et 'main'."
    exit 0
fi

echo $branch_name

if [[ ! $branch_name =~ ^(build|docs|feat|fix|perf|refactor|test)\/[A-Za-z0-9-]+\/.*$ ]]; then
    echo -e """
    \033[1;31mErreur : Nommage de votre branche non conforme !\033[0m
    \033[1;34mInformation : Le nom de votre branche ne suit pas la convention de PARK-IT.\033[0m
    
    \033[4;1mFormat Attendu\033[0m : \033[1;32m<TYPE>/<TICKET_ID>/DESCRIPTION\033[0m
    
    \033[4;1mTypes disponibles\033[0m :
    \033[1;32m- build
    - docs
    - feat
    - fix
    - perf
    - refactor
    - test\033[0m
    
    \033[4;1mExemple de nommage correct\033[0m : 
    
    \033[1;32m- feat/PI-170/mise-en-place-traefik\033[0m

    \033[1m⚠️ Si vous n'avez pas de numéro de ticket, il est fortement recommandé de créer le ticket\033[0m \033[1;34m(Voir Thibault ou Fabien)\033[0m

    \033[1mSi vraiment la création de ticket ne peut pas être faite, voici des exemples sans ticket correspondant :\033[0m

    \033[1;32m- fix/IA/function-returns-undefined
    - fix/BACKEND/function-returns-undefined
    - fix/FRONTEND/function-returns-undefined
    - fix/DEVOPS/function-returns-undefined\033[0m

    \033[1;34mVueillez renommer votre branche a l'aide de la commande suivante\033[0m \033[1;31m(En respectant la convention)\033[0m :

    \033[1;32m- git branch -m nouveau-nom-branche
    - git push origin nouveau-nom-branche\033[0m

    """
    exit 1
fi
