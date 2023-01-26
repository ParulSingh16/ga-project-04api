python manage.py dumpdata jwt_auth --output jwt_auth/seeds.json --indent=2;
python manage.py dumpdata partners --output partners/seeds.json --indent=2;
python manage.py dumpdata policies --output policies/seeds.json --indent=2;
python manage.py dumpdata purchased_policies --output purchased_policies/seeds.json --indent=2;