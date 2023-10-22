# Pizzami

## project setup

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd Pizzami
```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- create your env
```
cp .env.example .env
```

4- spin off docker compose
```
docker compose -f docker-compose.dev.yml up
```