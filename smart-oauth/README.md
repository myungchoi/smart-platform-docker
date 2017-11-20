# Docker build/deployment for OpenID server

  Note: Please note that we need to create a docker subnet. Refer to the README.md file in the upper directory.

The docker command below will create an image (if not exists) with tag name samrt-oauth:latest.

`$ sudo docker build -t smart-oauth .`

Run the image with the follwing docker command. This will create a contained from the image build with the previous command. 

`$ sudo docker run --name smart-oauth --net smart-net --ip 172.27.0.3 -p 8060:8060 --hostname smart-oauth --add-host smart-mysql:172.27.0.2 --add-host smart-oauth:172.27.0.3 -d smart-oauth:latest`
