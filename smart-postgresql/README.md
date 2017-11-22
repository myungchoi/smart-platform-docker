# PostgreSQL database for GT-FHIR. This container has a schema called "omop_v5", which contains a few
sample patient data. To support GT-FHIR, f_* table/view exist. To support context holder, some smart_* tables exists.
omop_v5 schema has OHDSI's OMOP v5 schema. 

`$ sudo docker build -t smart-postgres .`

# Run this image

`$ sudo docker run --name smart-postgres --net smart-net --ip 172.27.0.6 -p 5433:5432 --hostname smart-postgres -d smart-postgres:latest`
