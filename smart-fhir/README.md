# Docker build/deployment for GT-FHIR 

`$ sudo docker build -t smart-fhir .`

# Run the image.

`$ sudo docker run --name smart-fhir --net smart-net --ip 172.27.0.5 -p 8080:8080 --hostname smart-fhir --add-host smart-mysql:172.27.0.2 --add-host smart-oauth:172.27.0.3 -d smart-fhir:latest`
~
