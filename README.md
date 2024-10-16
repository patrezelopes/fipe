# fipe

use this examples on your .env file
```
MONGO_INITDB_ROOT_USERNAME=fipe
MONGO_INITDB_ROOT_PASSWORD=password
ME_CONFIG_MONGODB_ADMINUSERNAME=fipe
ME_CONFIG_MONGODB_ADMINPASSWORD=password
ME_CONFIG_MONGODB_URL=mongodb://fipe:password@mongo:27017/
ALLOWED_HOSTS=*
CORS_ORIGIN_WHITELIST=http://localhost:8080,http://localhost:8000
MONGO_URI=mongodb+srv://fipe:password@db
DB_HOST=db
DB_NAME=fipe
DB_USER=mongo_user
DB_PASS=mongo_pass
BROKER_HOST=rabbitmq
BROKER_USER=guest
BROKER_PASS=guest
BROKER_PORT=5672
QUEUE=events_queue
ROUTING_KEY=events
CELERY_BROKER_URL=amqp://rabbitmq:5672
DEBUG=True
```

### Up all container using docker compose
```
make up-all
```

### Up all container using docker compose
```
make logs
```