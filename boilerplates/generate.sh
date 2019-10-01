#!/bin/bash

GO_LANG="go"
PYTHON="python"
JAVA="java"
JAVASCRIPT="javascript"

ALLOWED_LANGUAGES=($GO_LANG $PYTHON $JAVA $JAVASCRIPT)

GREEN='\033[0;32m' 
RED='\033[0;31m' 
NOCOLOR='\033[0m' 

echo ""

if [[ ! " ${ALLOWED_LANGUAGES[*]} " == *" $1 "* ]]; then
    echo "Invalid language!!"
    echo "Use one of the languages below!"
    echo "${GREEN}${ALLOWED_LANGUAGES[*]}${NOCOLOR}"
    exit 0
fi


# Linguagem escolhida
language=$1
echo "Language selected: ${language}"
echo ""

# Retorno: Uma data no formato yyyy-mm-dd
currentDate=`date +%F`

# Substituindo o caracter '-' por '_'
dojoDir="${currentDate//-/_}"


echo "Creating directory..."
echo ""

errorDir="$(mkdir $dojoDir 2>&1)"

if [ "$errorDir" != "" ]; then
    echo "${RED}Erro: ${errorDir}${NOCOLOR}"
    echo ""
    exit 0
fi

echo "Copying the files to the directory ./${dojoDir} ..."
echo ""

erroCp=$(cp -R boilerplates/$1/. $dojoDir 2>&1)

if [ "$erroCp" != "" ]; then
    echo "${RED}Erro: ${erroCp}${NOCOLOR}"
    echo ""
    exit 0
fi

echo "Boilerplate successfully created: $GREEN$dojoDir$NOCOLOR"

cat TITLE
