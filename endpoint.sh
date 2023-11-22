#!/usr/bin/bash
python manage.py migrate --check
status=$?
if [[ status != 0 ]]; then
  python manage.py migrate
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${FOX_SUPERUSER_NAME}', '${FOX_SUPERUSER_EMAIL}', '${FOX_SUPERUSER_PWD}')"

fi
python manage.py collectstatic --no-input --clear
exec "$@"
