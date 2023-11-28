#!/bin/bash

hooks_folder="../.git/hooks"

cp samples/pre-push "$hooks_folder/"
cp samples/commit-msg "$hooks_folder/"

chmod +x "$hooks_folder/pre-push"
chmod +x "$hooks_folder/commit-msg"

chmod +x ./check_branch_norme.sh
chmod +x ./check_commit_norme.sh

echo -e "\033[1;32mHooks des conventions de branches et commits configurés avec succès.\033[0m"
