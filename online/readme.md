# Docker Compose
build image and push to docker hub
```sh
docker build -t <user>/<image_name> . 
docker push <user>/<image_name>
```

you can edit var1, var2, var3
```yml
version: '3'

services:
  demo:
      image: <user>/<image_name>
      restart: always
      environment:
        - var1=welcome to docker 101
        - var2=this is how we pass var between .py file
        - var3=0
      command: python -u src/main.py
```

after edited source code you must re-build docker compose
```sh
docker-compose up --build -d
```
