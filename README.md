pycv
====

Simple, short and slick multilanguage curriculum vitae generator in python.

Here you can see how it looks filled out:
[my cv](http://marek.szwalkiewicz.waw.pl/ "Marek Szwalkiewicz - Resume")

This script is based on Flask and Babel on python side with style added by
bootstrap and bootswatch.

This app should not be trated like something production ready ;). It is very
much BETA quality and will be (hopefully) expanded in the future.

Installation
============

Create virtualenv and pull requirements from `requirements` file with:

`$ pip install -r requirements`

Then you can run debug version with:

`$ python serve.py`

or you can look into examples folder to check sample config files for popular
web servers.

Configuration
=============

All you need to know and set is located in `translations` folder __init__ file.
Just open this file and read comments that are there to guide you through
the process.

After that you need to add languages (there is no "base" language!) using
`babel_tools.sh` script (just run it without arguments and read small usage
note). In this version every translation is going trough .po file - in future
I want to make some simple admin panel that will make translations easy.
For now - user poedit.
