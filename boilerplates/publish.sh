#!/bin/bash

# If any command on pipe fails, return failure
set -o pipefail

function yesno {
    unset response
    while [ "$response" != "y" ] && [ "$response" != "n" ]
    do
        echo -n "$@"
        echo -n " [y/n] "
        read response
        response=`echo $response | tr '[:upper:]' '[:lower:]'`
    done
    [ "$response" == "y" ] && return 0 || return 1
}

yesno "This will publish current branch code to master branch, continue?" || exit 0

# Retorno: Uma data no formato dd/mm/yyyy
currentDate=`date +%d/%m/%Y`
main_branch="master"

current_branch=$(git rev-parse --abbrev-ref HEAD)

if [ $current_branch != $main_branch ]; then
    echo "You should be at master. Please, move this branch's code to master. 😞"
    exit 1
fi

#Atualizando o repositório
echo "Updating repository"
git fetch --all
git pull origin $main_branch

#Commitando as mudanças feitas
echo "Commiting the day's dojo files"
git add .
git commit -m "Dojo do dia ${currentDate}"

git push origin $main_branch
echo "Your commits were pushed sucessfully ⛅"

exit 0