Simple image to asses if your deployment process works.

# Helm chart

In the chart folder, execute:

```
helm isntall pg-redis-fastapi .
```

You can check if the server is live by forwarding the port 8000

```
kubectl port-forward service/pg-redis-fastapi-chart 8000:8000
```

# API:
FastApi will be exposed on port 8000.
In order to run properly, required environement varaibles are:

- `DB_URI`: URL to connect to the postgres Database. (For instance: postgresql://dev:devpass@localhost:5432/db)
- `REDIS_HOST`: host of the redis server
- `REDIS_PASSWORD`: password for the redis server

3 endpoints are exposed:
- `/` : basic "Hello World" message
- `/db-connect`: Check if the app connects to the DB based on DB_URI
- `redis-connect`: Check if the app connects to Redis based on REDIS_HOST and REDIS_PASSWORD

# Frontend:

Frontend image will deliver a basic HTML page hitting the API.
To setup which server you want to send HTTP request to, use `API_HOST` environement variable


To fire up services : `docker-compose up -d`
Note to M1 users:
`export DOCKER_DEFAULT_PLATFORM=linux/amd64` is required before building the image.

