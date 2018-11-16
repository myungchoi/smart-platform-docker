FROM smartonfhir/patient-browser:node
ENV LAUNCHER_PORT="443"
ENV FHIR_VIEWER_PORT="80"
ENV HAPI_PORT_STU3="443"
ENV HAPI_PORT_STU2="443"
COPY ./smart-patientpicker /usr/share/nginx/html/config
CMD ["sh" "-c" "\"envsubst < /usr/share/nginx/html/config/gt-fhir.tpl > /usr/share/nginx/html/config/stu3-local.json5 && nginx -g 'daemon off;'\""]