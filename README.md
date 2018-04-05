# Flask Mailroom Application

## To Run

All commands to be run from inside the repository directory.
```
$ pip install -r requirements.txt
$ python setup.py
$ python main.py
```

## To Publish to Heroku

All commands to be run from inside the repository directory.
```
$ git init                # Only necessary if this is not already a git repository
$ heroku create flask-mailroom
Creating ⬢ flask-mailroom... done
https://flask-mailroom.herokuapp.com/ | https://git.heroku.com/flask-mailroom.git
$ git push heroku master  # If you have any changes or files to add, commit them before you push. 
[alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-mailroom (master)]$ git push heroku master  
Counting objects: 531, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (513/513), done.
Writing objects: 100% (531/531), 1.42 MiB | 765.00 KiB/s, done.
Total 531 (delta 79), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.4
remote: -----> Installing pip
remote: -----> Installing requirements with pip
remote:        Collecting click==6.7 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 1))
remote:          Downloading click-6.7-py2.py3-none-any.whl (71kB)
remote:        Collecting Flask==0.12.2 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 2))
remote:          Downloading Flask-0.12.2-py2.py3-none-any.whl (83kB)
remote:        Collecting itsdangerous==0.24 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 3))
remote:          Downloading itsdangerous-0.24.tar.gz (46kB)
remote:        Collecting Jinja2==2.10 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 4))
remote:          Downloading Jinja2-2.10-py2.py3-none-any.whl (126kB)
remote:        Collecting MarkupSafe==1.0 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 5))
remote:          Downloading MarkupSafe-1.0.tar.gz
remote:        Collecting peewee==3.2.2 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 6))
remote:          Downloading peewee-3.2.2.tar.gz (592kB)
remote:        Collecting psycopg2==2.7.4 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 7))
remote:          Downloading psycopg2-2.7.4-cp36-cp36m-manylinux1_x86_64.whl (2.7MB)
remote:        Collecting Werkzeug==0.14.1 (from -r /tmp/build_6d7e5b9e518b736578894f37632f37e9/requirements.txt (line 8))
remote:          Downloading Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
remote:        Installing collected packages: click, itsdangerous, Werkzeug, MarkupSafe, Jinja2, Flask, peewee, psycopg2
remote:          Running setup.py install for itsdangerous: started
remote:            Running setup.py install for itsdangerous: finished with status 'done'
remote:          Running setup.py install for MarkupSafe: started
remote:            Running setup.py install for MarkupSafe: finished with status 'done'
remote:          Running setup.py install for peewee: started
remote:            Running setup.py install for peewee: finished with status 'done'
remote:        Successfully installed Flask-0.12.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24 peewee-3.2.2 psycopg2-2.7.4
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 47.6M
remote: -----> Launching...
remote:        Released v3
remote:        https://flask-mailroom.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/flask-mailroom.git
 * [new branch]      master -> master

(env) [alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-mailroom (master)]$ git remote add pro git@heroku.com:flask-mailroom.git
(env) [alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-mailroom (master)]$ git remote add stage git@heroku.com:flask-mailroom.git
(env) [alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-mailroom (master)]$ git push stage master
(env) [alinafe.matenda@MBP-C02PRS2JFVH5-2 flask-mailroom (master)]$ git push pro master

$ heroku addons:create heroku-postgresql:hobby-dev
Database has been created and is available
 ! This database is empty. If upgrading, you can transfer
 ! data from another database with pg:copy
Created postgresql-elliptical-63721 as DATABASE_URL
Use heroku addons:docs heroku-postgresql to view documentation

$ heroku run python setup.py
$ heroku open
http://flask-mailroom.herokuapp.com/donations/
```
