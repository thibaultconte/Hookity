#!/bin/bash

hooks_folder=".git/hooks"

# Vérifier si les hooks existent avant de les supprimer
if [ -f "$hooks_folder/pre-push" ] || [ -f "$hooks_folder/commit-msg" ]; then
    rm -f "$hooks_folder/pre-push"
    rm -f "$hooks_folder/commit-msg"

    echo -e "\033[1;32mLes conventions Hookity à été désactivés avec succés.\033[0m"
else
    echo -e "\033[1;33mAucunes configurations Hookity était activées.\033[0m"
fi
