# SMART on FHIR Platform Installation

This is GT-FHIR research platform installation instruction. The following open-source implementations are used (Thank you! Open-source community!!!)

GT-FHIR: based on HAPI-FHIR and OMOP v5 CDM
OAuth server: based on HSPC Auth server
Patient picker (for context resolver): SMART on FHIR 

Custom network bridge information for docker containers to support SMART on FHIR
Docker command:

`$ sudo docker network create --subnet=172.27.0.0/16 smart-net`

Network Name: 	smart-net
Network: 	172.27.0.0/16

Host                 | IP         | DESC
-------------------- | ---------- | ------------------------------------
smart-mysql          | 172.27.0.2 | MySql Server for OpenID/OAuth server
smart-oauth          | 172.27.0.3 | OpenID/OAuth server
smart-patientpicker  | 172.27.0.4 | Patient Picker for context resolver
smart-fhir           | 172.27.0.5 | FHIR server with GT-FHIR (DSTU2) 
smart-postgresql     | 172.27.0.6 | PostgreSQL database for FHIR server
smart-pythonapp      | 172.27.0.7 | Sample SMART on FHIR app


Tips:
  When running image, assign IP.

`$ sudo docker run --name <container_name> --net <network_name> --ip <ip_we_want_to_assign> --hostname <hostname> --add-host <host_to_add> -it <image_name> bash`
