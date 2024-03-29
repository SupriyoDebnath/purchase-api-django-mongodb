## _Reference_

- [Official Docker Image Build Guide](https://docs.docker.com/engine/reference/commandline/image_build/)
- [Official Docker Volume Management Guide](https://docs.docker.com/storage/volumes/)

<br>

## _Build Image_
```sh
docker image build -t pm-app-image:2.0.0 .
```

## _Check Image_
```sh
docker image ls -a | grep pm-app-image
docker inspect pm-app-image:2.0.0
```

## _Create Volume_
```sh
docker volume create pm-app-media2
```

## _Check Volume_
```sh
docker volume ls | grep pm-app-media2
docker inspect pm-app-media2
```

## _Run Container_
```sh
docker run -d \
  --name pm-app-mongodb \
  --network pm-net \
  -p 8001:8001 \
  --mount type=volume,src=pm-app-media2,dst=/workspace/source/media \
  pm-app-image:2.0.0
```

## _Check Container_
```sh
docker container ls -a | grep pm-app-mongodb
docker inspect pm-app-mongodb
docker container logs pm-app-mongodb
docker exec -it pm-app-mongodb sh
 > whoami
 > ps -ef
 > exit
```

## _Run DRF Checks_
```sh
python3 manage.py migrate
python3 manage.py createsuperuser
```