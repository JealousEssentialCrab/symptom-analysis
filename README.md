## Coding Challenge

A small Flask/Angular Webapp.

Project requirements:

python3.6

node with npm 5+

pipenv

example (Ubuntu 16.04):

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6 python3.6-dev
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
apt install python3-pip
pip3 install pipenv

To setup project:

pipenv install --dev (if not using python3.6 by default, you must specify the python
path with the --python flag. e.g:
pipenv install --dev --python /usr/local/Cellar/python3/3.6.3/bin/python3)

to start:

./init_persistance.sh (only needs to be run once).
./start_server.sh


Once pipenv is installed, run the server with ./start_server.sh
