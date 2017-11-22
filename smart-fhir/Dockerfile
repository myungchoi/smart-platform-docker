FROM tomcat:alpine
RUN apk update
RUN apk add zip

RUN mkdir -p "/opt/app"
ADD *.xml /opt/app/
ADD gt-fhir-webapp*.war /opt/app/gt-fhir-webapp.war

# Copy GT-FHIR war file to webapps.
RUN cp /opt/app/gt-fhir-webapp.war $CATALINA_HOME/webapps/
RUN mkdir -p $CATALINA_HOME/webapps/gt-fhir-webapp/ && cd $CATALINA_HOME/webapps/gt-fhir-webapp/ && unzip $CATALINA_HOME/webapps/gt-fhir-webapp.war

# add/replace config xmls files for GT-FHIR into the WEB-INF/ directory. 
RUN  cp /opt/app/*.xml $CATALINA_HOME/webapps/gt-fhir-webapp/WEB-INF/

EXPOSE 8080
CMD ["catalina.sh", "run"]
