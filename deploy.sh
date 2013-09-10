#!/bin/bash
# deploy script
if [ "$1" = "staging" ]
then
    git push heroku-dev dev:master
elif [ "$1" = "production" ]
then
    git push heroku dev:master
else
    echo "Usage: ./deploy.sh (production|staging)"
fi
