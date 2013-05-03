#!/bin/bash

if [ "$1" == "extract" ]
then
    pybabel extract -F babel.cfg -o translations/messages.pot .
elif [ "$1" == "add" ]
then
    pybabel init -i translations/messages.pot -d translations -l $2
elif [ "$1" == "compile" ]
then
    pybabel compile -d translations
elif [ "$1" == "update" ]
then
    pybabel update -i translations/messages.pot -d translations
else
    echo "Simple script abstracting pybabel commands for pycv.
Usage:

extract - extract messages from source files and generate a POT file
add [lang] - create new message catalogs from a POT file with a given language
compile - compile message catalogs to MO files
update - update existing message catalogs from a POT file"
fi