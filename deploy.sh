#!/bin/bash
# deploy script
if [ "$1" = "init" ]
then
    git remote remove heroku 2> /dev/null
    git remote remove heroku-dev 2> /dev/null
    git remote add heroku git@heroku.com:nccu-study-net.git
    git remote add heroku-dev git@heroku.com:nccu-study-net-dev.git 
    echo "Set heroku, heroku-dev in your git remotes."
elif [ "$1" = "staging" ]
then
    git push heroku-dev master
elif [ "$1" = "production" ]
then
    git push heroku production:master
else
    echo "Usage: ./deploy.sh (production|staging)"
fi
