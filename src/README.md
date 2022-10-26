# Zalf_Geonode



## Setup Geonode project to run for development

This describes how to start a GeoNode Project to run in development mode.

### Removing old containers and volume artefacts

Make that no containers or volumes are already build and lying around before setting up the dev environment ...

removing old containers:

```
TMP_PROJECT_NAME="zalf_geonode" ; for i in `docker ps -a -f name=$TMP_PROJECT_NAME* --format "{{.Names}}"` ; do docker stop $i; docker rm $i  ;done
```

removing old volumes and containers via:
```
TMP_PROJECT_NAME="zalf_geonode" ; for i in `docker volume ls -f name=$TMP_PROJECT_NAME* --format "{{.Name}}"` ; do docker volume rm $i  ;done
```

### Starting docker containers

```
docker-compose build --no-cache
```

```
docker-compose up -d
```

```
docker-compose -f docker-compose.yml -f .devcontainer/docker-compose.yml up
```


```
docker exec -it django4zalf_geonode bash -c "python manage.py runserver 0.0.0.0:8000"
```