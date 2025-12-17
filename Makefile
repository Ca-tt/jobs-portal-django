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

static-prod:
	python manage.py collectstatic --settings=jobs_portal.settings.prod --noinput

requirements-prod:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

migrate-prod:
	python manage.py migrate --settings=jobs_portal.settings.prod

prod-prep: 
	migrate-prod static-prod

check-prod:
	python manage.py check --settings=jobs_portal.settings.prod

activate-venv-prod:
	source ~/.venvs/myvenv/bin/activate

env-prod:
	chmod +x ./bash/make_env_prod.sh && ./bash/make_env_prod.sh

deploy-check:
	python manage.py check --deploy --settings=jobs_portal.settings.prod
