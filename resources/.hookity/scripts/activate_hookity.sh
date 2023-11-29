#!/bin/bash

hooks_folder=".git/hooks"

cp .hookity/samples/pre-push "$hooks_folder/"
cp .hookity/samples/commit-msg "$hooks_folder/"

chmod +x "$hooks_folder/pre-push"
chmod +x "$hooks_folder/commit-msg"

chmod +x .hookity/check_branch_norme.sh
chmod +x .hookity/check_commit_norme.sh

echo -e "\033[1;32mLes Hooks de convention de nommage Hookity Git ont été activé avec succés.\033[0m"
