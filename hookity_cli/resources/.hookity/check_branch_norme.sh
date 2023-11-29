#!/bin/bash

config_file="$(git rev-parse --show-toplevel)/.hookity/hookity_config.json"

if [ -f "$config_file" ]; then
    config=$(cat "$config_file")
    branch_type_authorized=($(echo "$config" | jq -r  '.branch_type_autorized[]'))
    organization_name=$(echo "$config" | jq -r '.organization_name')
else
    echo "Erreur : Fichier de configuration hookity_config.json introuvable."
    exit 1
fi

branch_name=$(git symbolic-ref HEAD --short 2>/dev/null)

types_regex=$(IFS='|'; echo "${branch_type_authorized[*]}")
branch_regex="^($types_regex)\/+[A-Za-z0-9-]"

if [[ $branch_name == "develop" || $branch_name == "main" ]]; then
    echo "Validation de convention Hookity ignorée pour les branches 'develop' et 'main'."
    exit 0
fi

if [[ ! $branch_name =~ $branch_regex ]]; then
echo -e """
\033[1;31mErreur : Nommage de votre branche non conforme à la convention !\033[0m
\033[1;34mInformation : Le nom de votre branche ne suit pas la convention de ${organization_name}.\033[0m

\033[4;1mFormat minimal attendu\033[0m : \033[1;32m<TYPE>/<DESCRIPTION>\033[0m

\033[4;1mTypes disponibles\033[0m :

\033[1;32m- ${branch_type_authorized[*]}\033[0m

\033[4;1mExemple de nommage correct\033[0m : 

"""
for i in ${branch_type_authorized[*]}
do
    echo -e "\033[1;32m $i\033[0m/\033[1;34mas_you_want\033[0m"
done
echo -e """

\033[1m ⚠️ Si vous avez un numéro de ticket à renseigner, vous pouvez le mettre dans le nom de votre branche\033[0m

\033[4;1mExemple de nommage avec numéro de ticket\033[0m : 
"""

for i in ${branch_type_authorized[*]}
do
    echo -e "\033[1;32m $i/\033[1;34mIssue_987\033[0m/\033[1;32mas_you_want\033[0m"
done


echo -e """
\033[1m ⚠️ Si vous n'avez pas de numéro de ticket à renseigner, mais que vous souhaitez mettre 
le nom de votre pôle de developpement, vous pouvez le faire aussi comme ceci\033[0m

\033[4;1mExemple de nommage avec pôle de développement\033[0m :
"""
pole_developpement=("IA" "BIG-DATA" "DEVOPS" "BACKEND" "FRONTEND" "APPLICATION")
counter=0
for ((i=0; i<${#branch_type_authorized[@]}; i++))
do
    type=${branch_type_authorized[$i]}
    pole=${pole_developpement[$counter]}
    if [ -z "$pole" ]; then
        counter=0
    else
        echo -e "\033[1;32m$type/\033[1;34m$pole\033[0m/\033[1;32mas_you_want\033[0m"
        ((counter++))
    fi
done

echo -e """
\033[1;34mVueillez renommer votre branche à l'aide de la commande suivante\033[0m \033[1;31m(En respectant la convention)\033[0m :

\033[1;32m- git branch -m nouveau-nom-branche
- git push origin nouveau-nom-branche\033[0m

"""
exit 1
fi