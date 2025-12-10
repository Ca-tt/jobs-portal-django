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