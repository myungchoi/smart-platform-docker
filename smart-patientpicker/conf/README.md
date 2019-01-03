# Docker build/deployment for Patient Picker app
  Note: This app is to be used as a context resolver. 

The docker command below will create an image

`$ sudo docker build -t smart-patientpicker .`

Run the image with the following docker command. This will create a container from the image build with the previous command.

`$ sudo docker run --name smart-patientpicker --net smart-net --ip 172.27.0.4 -p 8094:8094 --hostname smart-patientpicker --add-host smart-mysql:172.27.0.2 --add-host smart-oauth:172.27.0.3 -d smart-patientpicker:latest`
