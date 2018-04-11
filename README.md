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
$ heroku create flask-mailroom-stage
$ heroku create flask-mailroom-pro
$ git remote add pro git@heroku.com:flask-mailroom-pro.git
$ git remote add stage git@heroku.com:flask-mailroom-stage.git
$ git push stage master
$ git push pro master

$ heroku addons:create heroku-postgresql:hobby-dev --app flask-mailroom-pro
$ heroku addons:create heroku-postgresql:hobby-dev --app flask-mailroom-stage
$ heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
$ heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
$ heroku run python setup.py --remote stage
$ heroku run python setup.py --remote pro
$ heroku open --app flask-mailroom-stage
$ heroku open --app flask-mailroom-pro
$ http://flask-mailroom-pro.herokuapp.com/donations/
$ http://flask-mailroom-stage.herokuapp.com/donations/
$ heroku run python main.py --app flask-mailroom-stage
$ heroku run python main.py --app flask-mailroom-pro

```
