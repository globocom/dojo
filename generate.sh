#!/bin/bash

GO_LANG="go"
PYTHON="python"
JAVA="java"
JAVASCRIPT="javascript"

ALLOWED_LANGUAGES=($GO_LANG $PYTHON $JAVA $JAVASCRIPT)

echo ""

if [[ ! " ${ALLOWED_LANGUAGES[*]} " == *" $1 "* ]]; then
    echo "Linguagem inválida!!"
    echo "Apenas as linguagens a seguir são válidas!"
    echo "LINGUAGENS: ${ALLOWED_LANGUAGES[*]}"
    exit 0
fi


# Linguagem escolhida
language=$1
echo "Linguagem escolhida ${language}"
echo ""

# Retorno: Uma data no formato yyyy-mm-dd
currentDate=`date +%F`

# Substituindo o caracter '-' por '_'
dojoDir="${currentDate//-/_}"


echo "Criando o diretório..."
echo ""

errorDir="$(mkdir $dojoDir 2>&1)"

if [ "$errorDir" != "" ]; then
    echo "Erro: ${errorDir}"
    echo ""
    exit 0
fi

echo "Copiando arquivos para a pasta..."
echo ""

erroCp=$(cp -R boilerplates/$1/. $dojoDir 2>&1)

if [ "$erroCp" != "" ]; then
    echo "Erro: ${erroCp}"
    echo ""
    exit 0
fi

cat TITLE
