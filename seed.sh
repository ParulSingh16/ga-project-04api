#!/bin/bash

echo "dropping database"
dropdb insurance

echo "creating database"
createdb insurance

python manage.py makemigrations

python manage.py migrate

echo "inserting jwt_auth"
python manage.py loaddata jwt_auth/seeds.json

echo "inserting partners"
python manage.py loaddata partners/seeds.json

echo "inserting policies"
python manage.py loaddata policies/seeds.json

echo "inserting purchased_policies"
python manage.py loaddata purchased_policies/seeds.json
