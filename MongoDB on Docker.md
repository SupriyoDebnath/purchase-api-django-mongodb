## _Reference_

- [MongoDB Docker Image ](https://hub.docker.com/_/mongo)
- [Official Docker Network Setup Guide](https://docs.docker.com/network/)
- [Official Docker Volume Management Guide](https://docs.docker.com/storage/volumes/)

<br>

## _Pull Image_
```sh
docker pull mongo:latest
```

## _Check Image_
```sh
docker image ls -a | grep mongo
docker inspect mongo:latest
```

## _Create Network_
```sh
docker network create pm-net
```

## _Check Network_
```sh
docker network ls | grep pm-net
docker inspect pm-net
```

## _Create Volume_
```sh
docker volume create pm-db2-data
docker volume create pm-db2-config
```

## _Check Volume_
```sh
docker volume ls | grep pm-db2-data pm-db2-config
docker inspect pm-db2-data
docker inspect pm-db2-config
```

## _Run Container_
```sh
docker run -d \
  --name pm-db2 \
  -e MONGO_INITDB_ROOT_USERNAME=pm-user \
  -e MONGO_INITDB_ROOT_PASSWORD=pmuser@2021 \
  --network pm-net \
  -p 27017:27017 \
  --mount type=volume,src=pm-db2-data,dst=/data/db \
  --mount type=volume,src=pm-db2-config,dst=/data/configdb \
  mongo:latest
```

## _Check Container_
```sh
docker container ls -a | grep pm-db2
docker inspect pm-db2
docker container logs pm-db2
docker exec -it pm-db2 sh
 > whoami
 > ps -ef
 > exit
```

## _Check MongoDB Installation_
```sh
mongod --version
```