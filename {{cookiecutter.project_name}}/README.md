# Pizzami

## project development setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd Pizzami
```

2- create your env
```
cp .env.example .env
```

3- spin off docker compose
```
docker compose -f docker-compose.dev.yml up
```

4- make migrations
```
python manage.py makemigrations
python manage.py migrate
```

5- run project
```
python manage.py runserver
```