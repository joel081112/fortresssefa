# fortresssefa website

This site is not currently uploaded anywhere

This is a great template that I hope to have in the future


# _______for another machine take these steps_______ #
delete all migrations
delete local postgres table

 might have to manage.py makemigrations DEMOAPP

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


if on pgadmin follow the tutorial to backup as sql file and then as tar file
then restore tar file into other machine's pgadmin
