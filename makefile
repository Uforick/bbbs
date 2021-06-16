run:
	python manage.py runserver

su:
	bash -c \
	"DJANGO_SUPERUSER_USERNAME=admin \
	DJANGO_SUPERUSER_PASSWORD=admin \
	DJANGO_SUPERUSER_EMAIL=admin@email.fake \
	python manage.py createsuperuser --noinput"

prepare:
	python manage.py makemigrations --noinput
	python manage.py migrate --noinput
	make su
	python manage.py collectstatic --noinput

prepare_in_docker:
	docker-compose exec backend make prepare