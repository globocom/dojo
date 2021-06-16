#!/bin/bash

PROGRAM_NAME="$(basename $0)"

GO_LANG="go"
PYTHON="python"
JAVA="java"
JAVASCRIPT="javascript"
RUST="rust"
PHP="php"
RUBY="ruby"
R="r"

ALLOWED_LANGUAGES=($GO_LANG $PYTHON $JAVA $JAVASCRIPT $RUST $PHP $RUBY $R)

GREEN='\033[0;32m' 
RED='\033[0;31m' 
NOCOLOR='\033[0m' 

display_usage() {
    echo "Usage: ${PROGRAM_NAME} [OPTIONS] LANGUAGE"
    echo ""
    echo "  Copies the boilerplate from the given language into a new"
    echo "  directory named as the current date."
    echo ""
    echo "Options:"
    echo "  -h, --help    Show this message and exit."
    echo ""
    echo "Language:"
    echo "  Use one of the languages below!"
    echo -e "  ${GREEN}${ALLOWED_LANGUAGES[*]}${NOCOLOR}"
    exit "${1:-1}"
}

[ -z "$1" ] && display_usage

([ "-h" == "$1" ] || [ "--help" == "$1" ]) && display_usage 0

if [[ ! " ${ALLOWED_LANGUAGES[*]} " == *" $1 "* ]]; then
    echo "Invalid language!!"
    echo "Use one of the languages below!"
    echo -e "${GREEN}${ALLOWED_LANGUAGES[*]}${NOCOLOR}"
    exit 1
fi

# Linguagem escolhida
language=$1
echo "Selected language: ${language}"
echo ""

# Retorno: Uma data no formato yyyy-mm-dd
currentDate=`date +%F`

# Substituindo o caracter '-' por '_'
dojoDir="${currentDate//-/_}"

echo "Creating directory..."
echo ""

errorDir="$(mkdir $dojoDir 2>&1)"

if [ "$errorDir" != "" ]; then
    echo -e "${RED}Error: ${errorDir}${NOCOLOR}"
    echo ""
    exit 1
fi

echo "Copying the files to the directory ./${dojoDir} ..."
echo ""

erroCp=$(cp -R boilerplates/$1/. $dojoDir 2>&1)

if [ "$erroCp" != "" ]; then
    echo -e "${RED}Error: ${erroCp}${NOCOLOR}"
    echo ""
    exit 1
fi

# set current date inside dojo.yml
sed -i "s@date: #yyyy-mm-dd@date: ${currentDate}@" "$dojoDir/dojo.yml"

echo -e "Boilerplate successfully created: ${GREEN}${dojoDir}${NOCOLOR}"

cat TITLE
