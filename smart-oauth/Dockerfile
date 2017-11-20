FROM openjdk:8-jdk-alpine
ADD hspc-reference-auth-server-webapp-*.war app.war
ADD jetty-runner.jar jetty-runner.jar
ADD jetty.xml jetty.xml
ENV JAVA_OPTS=""
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Dspring.profiles.active=local,users-local -jar jetty-runner.jar --config jetty.xml app.war" ]
