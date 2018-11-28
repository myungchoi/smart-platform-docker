FROM smartonfhir/patient-browser:node
ENV LAUNCHER_PORT="443"
ENV FHIR_VIEWER_PORT="80"
ENV HAPI_PORT_STU3="443"
ENV HAPI_PORT_STU2="443"
RUN mkdir /usr/share/nginx/html/smart-patientpicker && mv /usr/share/nginx/html/config /usr/share/nginx/html/smart-patientpicker && mv /usr/share/nginx/html/examples /usr/share/nginx/html/smart-patientpicker && mv /usr/share/nginx/html/img /usr/share/nginx/html/smart-patientpicker && mv /usr/share/nginx/html/js /usr/share/nginx/html/smart-patientpicker && mv /usr/share/nginx/html/vendor /usr/share/nginx/html/smart-patientpicker
COPY ./conf /usr/share/nginx/html/smart-patientpicker/config
COPY ./conf /usr/share/nginx/html/smart-patientpicker/examples/config
COPY /usr/share/nginx/html/smart-patientpicker/vendor /usr/share/nginx/html/smart-patientpicker/js/vendor
RUN sh -c "envsubst < /usr/share/nginx/html/smart-patientpicker/config/stu3-local.tpl > /usr/share/nginx/html/smart-patientpicker/config/stu3-local.json5"
#CMD ["sh" "-c" "\"envsubst < /usr/share/nginx/html/smart-patientpicker/config/stu3-local.tpl > /usr/share/nginx/html/smart-patientpicker/config/stu3-local.json5 && nginx -g 'daemon off;'\""]
#CMD ["nginx" "-g" "'daemon off;'"]