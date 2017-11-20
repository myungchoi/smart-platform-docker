This mysql container is to be used with hspc's auth server (MITREID based server).

USE THE FOLLOWING COMMAND TO RUN DOCKER. This will download image(s) and create a container with the name "smart-mysql" Database will also be created. See env.list for the database created and username/password (including root password for the database).

The env.list has a database setup that will be used by SMART on FHIR OAuth server to store configurations and user info.

Run follow to login to shell:

`$ sudo docker exec -it smart-oauth bash`

Here is how to run the image:

`$ sudo docker run --name smart-mysql --net smart-net --env-file env.list --ip 172.27.0.2 -p 8306:3306 --hostname smart-mysql -d mysql:5.6 --character-set-server=latin1 --collation-server=latin1_swedish_ci`
