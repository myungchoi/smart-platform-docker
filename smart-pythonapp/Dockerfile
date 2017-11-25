FROM ubuntu:16.04

# Update OS
RUN sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y upgrade
 
# Install Python
RUN apt-get install -y python-dev python-pip
RUN pip install --upgrade pip 

# Add requirements.txt
ADD client-py-FHIR-1.8.0 client-py
 
# Install app requirements
RUN cd /client-py && pip install -r requirements.txt && pip install -r requirements_flask_app.txt
 
# Set the default directory for our environment
ENV HOME /client-py
WORKDIR /client-py
 
EXPOSE 8000
ENTRYPOINT ["python", "flask_app.py"]
