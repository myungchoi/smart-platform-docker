# Use the Postgres image as a base
FROM postgres:alpine

# Define environment variable
#ENV POSTGRES_USER omop_v5
ENV POSTGRES_PASSWORD i3lworks
#ENV POSTGRES_DB omop_v5

# Add a loadDb.sh to docker-entrypoint-initdb.d so it is run at the end of the start up process to configure the database
ADD loadDb.sh /docker-entrypoint-initdb.d/loadDb.sh
RUN chmod -v a+rwx /docker-entrypoint-initdb.d/loadDb.sh

# Add omop_v5_dump.tgz to the /opt/data/ folder
RUN mkdir -p "/opt/data"
ADD omop_v5_dump.tgz /opt/data/omop_v5_dump.tgz
ADD *.sql /opt/data/
RUN chmod -R -v a+rwx /opt/data
