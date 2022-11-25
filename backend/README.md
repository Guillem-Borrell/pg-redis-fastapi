# Install 

```
pip install -u pip
pip install -e .
```

# Run
```
export DB_URI=postgresql://dev:devpass@localhost:5432/db
export REDIS_HOST=localhost
export REDIS_PASSWORD=devpass
./start.sh
```

Your server is up on port 8000