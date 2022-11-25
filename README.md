Simple image to asses if your deployment process works.

FastApi will be exposed on port 8000.
In order to run properly, required environement varaibles are: 

- `DB_URI`: URL to connect to the postgres Database. (For instance: postgresql://dev:devpass@localhost:5432/db)
- `REDIS_HOST`: host of the redis server
- `REDIS_PASSWORD`: password for the redis server

3 endpoints are exposed: 
- `/` : basic "Hello World" message
- `/db-connect`: Check if the app connects to the DB based on DB_URI
- `redis-connect`: Check if the app connects to Redis based on REDIS_HOST and REDIS_PASSWORD
-/db-connect:


To fire up services : `docker-compose up -d`