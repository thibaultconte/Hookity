#!/bin/bash

config_file="$(git rev-parse --show-toplevel)/.hookity/hookity_config.json"

if [ -f "$config_file" ]; then
    config=$(cat "$config_file")
    organization_name=$(echo "$config" | jq -r '.organization_name')
    commit_type_authorized=($(echo "$config" | jq -r  '.commit_type_autorized[]'))
    commit_scope_authorized=($(echo "$config" | jq -r  '.commit_scope_authorized[]'))
    
else
    echo "Erreur : Fichier de configuration hookity_config.json introuvable."
    exit 1
fi

if [ "$commit_scope_authorized" = "" ]; then
    commit_scope_authorized=".*"
fi

commit_message=$(cat .git/COMMIT_EDITMSG)

commit_type_regex=$(IFS="|" ; echo "${commit_type_authorized[*]}")
commit_scope_regex=$(IFS="|" ; echo "${commit_scope_authorized[*]}")
commit_regex="^($commit_type_regex)(\(($commit_scope_regex)\))?:[[:space:]]+.*"

if ! [[ $commit_message =~ $commit_regex ]]; then
echo -e """
\e[1;33mVotre message de commit actuel : '"$commit_message"'\033[0m

\033[1;31mErreur : Nommage de votre commit non conforme !\033[0m
\033[1;34mInformation : Votre message de commit ne suit pas la convention ${organization_name}\033[0m

\033[4;1mFormat Attendu\033[0m : \033[1;32mCOMMIT_TYPE(COMMIT_SCOPE): <COMMIT_SHORT_DESCR>\033[0m

\033[4;1mTypes de commit disponibles\033[0m :
"""
for i in ${commit_type_authorized[*]}
do
    echo -e "\033[1;32m- $i\033[0m"
done
echo -e """
\033[4;1mScopes de commit disponibles\033[0m :
"""
if [ "$commit_scope_authorized" = ".*" ]; then
    echo -e "\e[1;33m Vous pouvez mettre ce que vous souhaitez, déduisez par logique et soyez cohérents, faites en fonction du service, de l'outil,
du pôle, etc... Sur lequel vous travaillez.\033[0m"
    else
        for i in ${commit_scope_authorized[*]}
        do
            echo -e "\033[1;32m- $i\033[0m"
        done

fi

echo -e """

\033[4;1mExemple de messages de commit corrects\033[0m : 
"""
if [ "$commit_scope_authorized" = ".*" ]; then
        for type in "${commit_type_authorized[@]}"; do
        echo -e "\033[1;32m- $type(test-api): Description du commit\033[0m"
        done
    else
        for type in "${commit_type_authorized[@]}"; do
        echo -e "\033[1;32m- $type($commit_scope_authorized): Description du commit\033[0m
        "
        done

fi

exit 1
fi

exit 0