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
$ git push heroku master  # If you have any changes or files to add, commit them before you push. 
$ git push heroku master  
$ git remote add pro git@heroku.com:flask-mailroom.git
$ git remote add stage git@heroku.com:flask-mailroom.git
$ git push stage master
$ git push pro master

$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku run python setup.py
$ heroku open
http://flask-mailroom.herokuapp.com/donations/
heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
heroku run python main.py --app flask-mailroom

```
