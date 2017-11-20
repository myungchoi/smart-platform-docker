FROM node:alpine
RUN apk update
RUN apk add bash
RUN apk add git
RUN mkdir -p /opt/app
RUN cd /opt/app && git clone https://myungchoi@bitbucket.org/myungchoi/patient-picker.git
WORKDIR /opt/app/patient-picker
RUN npm install
ENTRYPOINT ["sh", "-c", "npm run serve"]
