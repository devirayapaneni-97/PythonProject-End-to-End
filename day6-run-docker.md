

#### How to Build a Docker Image from a Dockerfile:

1. Create a working directory and necessary files:

```Create a directory named "template" and navigate to it.
Inside the "template" directory, create an "index.html" file.
```
2. Select a base image:
```Use the FROM instruction in your Dockerfile to select a base image. 
For example:

FROM python3.9-slim
```

3. Create a Dockerfile:
```
Create a file named "Dockerfile" in the "template" directory.
```

4. Add build instructions to the Dockerfile:
```Within the Dockerfile, specify:
Base image.
Working directory.
Required packages and dependencies.
Copying of code (COPY . .).
Entry point.
```

5. Build the image using the Docker build command:

```Execute the following command to build the Docker image:

docker build -t my_flask-app . 
```

6. Verify the built Docker image:
```
Use the command 'docker image ls' to verify that the image was successfully built.
```
7. Listing all Docker Images on the System:
```   
Use the command 'docker image ls' to list all Docker images on the system.
```

8. Running a Docker Container from an Image:
```
Execute the following command to run a Docker container from an image:
'docker run -p 5000:5000 --name my-flask-container my_flask-app'
```
9. Listing all Running Docker Containers:
```
Use 'docker container ls' to list all running Docker containers.
```

10. Listing all Containers (Including Stopped Ones)
```
To list all containers, including stopped ones, use the command 'docker container ls -a'
```

11. Stopping a Running Docker Container:
```
To Stop a running Docker container use 'docker container stop my-flask-container'
```
12. Removing a Docker Container:
```
Remove a Docker container with 'docker container rm my-flask-container'
Remove a Docker image with 'docker image rm my_flask-app'
```

13. Executing a Command Inside a Running Docker Container:
```
Use the 'docker exec' command to execute a command inside a running Docker container. 
For example:
'docker exec my-flask-container uptime'

docker exec: This is the Docker command used to execute a command inside a running container.

my-flask-container: This is the name of the Docker container where you want to execute the command. In this case, it's assumed that there is a Docker container running with the name my-flask-container.

uptime: This is the command that you want to execute inside the container. 
The uptime command typically displays the current time, how long the system has been running,
 how many users are currently logged in,
and the system load averages for the past 1, 5, and 15 minutes.
```

14. Checking Docker Running Container Logs:
```
To view logs of a Docker running container, use the command 'docker logs my-flask-container'
```
