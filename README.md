# fortresssefa website

This site is not currently uploaded anywhere

# For up to date code on your machine `git pull origin main`

## created with python3.7
For vscode (freeapp)

open new window

_clone repository_

Use these commands

git branch newBranch

git checkout newBranch

(python 3.7 download required)

py -3.7 -m venv myenv

source myenv/scripts/activate

pip install -r requirements.txt



# _______for another machine take these steps_______ #
delete all migrations

Download PGAdmin and PostrgreSQL

Need to set up a PGAdmin database account and table

`CREATE ROLE username WITH LOGIN PASSWORD 'quoted password';`

`CREATE DATABASE databasename;`

`GRANT ALL PRIVILEGES ON DATABASE databasename TO username;`

delete local postgres table, if applicable

 might have to manage.py makemigrations DEMOAPP


 might have to manage.py migrate DEMOAPP
 
might have to comment out models.py in demoapp
python manage.py migrate --run-syncdb

might have to recomment back in the models.py
python manage.py makemigrations
python mange.py migrate
python manage.py migrate --run-syncdb

python manage.py loaddata db.json


python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e
      auth.permission -e wagtailcore.groupcollectionpermission --indent 4 > db.json
python manage.py loaddata db.json


## Command help

For updated Branch code when not on main branch just  type `git pull origin main`

C:\Users\aszka>cd source/repos

C:\Users\aszka\source\repos>cd fortresssefa

C:\Users\aszka\source\repos\fortresssefa>cd myenv

C:\Users\aszka\source\repos\fortresssefa\myenv>cd scripts

C:\Users\aszka\source\repos\fortresssefa\myenv\Scripts>activate

(myenv) C:\Users\aszka\source\repos\fortresssefa\myenv\Scripts>cd ..

(myenv) C:\Users\aszka\source\repos\fortresssefa\myenv>cd ..

(myenv) C:\Users\aszka\source\repos\fortresssefa>py manage.py runserver

# FINALLY

Make sure the database username and password match local PGADMIN credentials in settings.py

You will know this is wrong if the error shown for wrong details when running commands such as makemigrations or runserver!!

### pip freeze > requirements.txt
