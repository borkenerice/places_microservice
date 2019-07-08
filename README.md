# Juego de Tornos Places Microservice
Microservice that exposes an API to perform CRUD operations over the Places Database

## Requirements
Having [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Installation

1. Build and run the project: `docker-compose up --build -d`
2. Init database:

   `docker-compose exec places_api flask db init`
   
   `docker-compose exec places_api flask db migrate`
   
   `docker-compose exec places_api flask db upgrade`
   
After these steps you should be able to access a swagger ui through the url http://0.0.0.0:8082/api/ui

## Optional

The database is empty, but you can fill it with some examples running:

`docker-compose exec places_api python utils/populate_database.py`


## Tests

Used pytest and fixtures to test the application.