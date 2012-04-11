web: python app/manage.py collectstatic --noinput; python uws/manage.py run_gunicorn --workers=4 --bind=0.0.0.0:$PORT uws/settings.py
