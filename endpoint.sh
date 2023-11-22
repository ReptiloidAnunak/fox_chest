#!/usr/bin/bash
source .env

python manage.py migrate --check
status=$?
if [[ status != 0 ]]; then
  python manage.py migrate
  python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(os.environ['FOX_SUPERUSER_NAME'], os.environ['FOX_SUPERUSER_EMAIL'], os.environ['FOX_SUPERUSER_PWD'])"

fi
#python manage.py collectstatic --no-input --clear
exec "$@"
