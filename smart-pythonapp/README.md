# Docker build/deployment for client-py 

`$ sudo docker build -t smart-pythonapp .`

# Run the image.

`$ sudo docker run --name smart-pythonapp --net smart-net --ip 172.27.0.7 -p 8000:8000 --hostname smart-pythonapp -d smart-pythonapp:latest`
~
