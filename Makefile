run:
	poetry run python manage.py runserver

check:
	poetry run python manage.py check

shell:
	poetry run python manage.py shell

showmigrations:
	poetry run python manage.py showmigrations

newapp:
	poetry run python manage.py startapp $(name)

superuser:
	poetry run python manage.py createsuperuser

psql:
	psql -U postgres -d django_store

migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate && poetry run python manage.py runserver 

changepass:
	poetry run python manage.py changepassword $(user)

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

# 1. Create .env file on production
# 2. Check for deploy-related issues
# 3. Collect static files
# 4. Apply database migrations

env-prod:
	chmod +x ./bash/make_env_prod.sh && ./bash/make_env_prod.sh

deploy-check:
	python manage.py check --deploy --settings=jobs_portal.settings.prod

check-prod:
	python manage.py check --settings=jobs_portal.settings.prod

static-prod:
	python manage.py collectstatic --settings=jobs_portal.settings.prod --noinput

migrate-prod:
	python manage.py makemigrations --settings=jobs_portal.settings.prod && python manage.py migrate --settings=jobs_portal.settings.prod

superuser-prod:
	python manage.py createsuperuser --settings=jobs_portal.settings.prod

run-prod:
	python manage.py runserver --settings=jobs_portal.settings.prod

# Helpers
activate-venv-prod:
	source ~/.venvs/myvenv/bin/activate

