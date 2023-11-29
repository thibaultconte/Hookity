#!/bin/bash

hooks_folder=".git/hooks"
hookity_folder=".hookity"

if [ -f "$hooks_folder/pre-push" ] || [ -f "$hooks_folder/commit-msg" ]; then
    rm -f "$hooks_folder/pre-push"
    rm -f "$hooks_folder/commit-msg"
    echo -e "\033[1;32mLes conventions Hookity à été désactivés avec succés.\033[0m"
else
    echo -e "\033[1;33mAucunes configurations Hookity n'était activé.\033[0m"
fi

if [ -d "$hookity_folder" ]; then
    rm -rf "$hookity_folder"
    echo -e "\033[1;32mHookity a été désinstaller complétement de votre repository git.\033[0m"
else
    echo -e "\033[1;33mHookity n'existe pas ou bien n'a pas été initialiser.\033[0m"
fi
