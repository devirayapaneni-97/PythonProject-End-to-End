#### How to setup docker container 

+ Install the docker engine using `docker desktop`
+ Check if the docker installation is complete, enter the below in GIT
    ```
    docker --version
    ```
+ The below is used to build my docker image.
  ```
  docker build -t my-flask-app .
  ```
+ The below is used to verify my docker image.
  ```
  docker image ls
  ```
+ The below is used to run my container with docker image.
  ```
  docker run --name my-flask-container my-flask-app
  ```
+ The below is used to verify docker container
  ```
  docker ps
  ```