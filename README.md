To reproduce problem:

tox -e py27 # This runs no problem
tox -e py27 # Second time through, wont work

mv tox.ini_works tox.ini
rm -r .tox
tox -e py27 # This runs no problem
tox -e py27 # This works too!



