.PHONY: server

app:
	docker-compose up -d
	
	sleep 5

	docker exec api python manage.py makemigrations
	docker exec api python manage.py migrate
	docker exec api python manage.py create_data