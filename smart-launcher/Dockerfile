FROM smartonfhir/smart-launcher
ENV NODE_ENV="production"
#ENV HOST="gt-apps.hdap.gatech.edu";
#ENV AUTH_BASE_URL=""
#ENV FHIR_BASE_URL=""
ENV LAUNCHER_BASE_URL="https://smartlauncher.hdap.gatech.edu/"
ENV BASE_URL="https://smartlauncher.hdap.gatech.edu/"
#ENV LAUNCHER_BASE_URL="https://gt-apps.hdap.gatech.edu/smart-launcher"
#ENV BASE_URL="https://gt-apps.hdap.gatech.edu/smart-launcher"
ENV FHIR_SERVER_R3="https://apps.hdap.gatech.edu/gt-fhir/fhir"
#ENV FHIR_SERVER_R3="http://localhost:${HAPI_PORT_STU3}/baseDstu3"
ENV FHIR_SERVER_R3_INTERNAL="https://apps.hdap.gatech.edu/gt-fhir/fhir"
ENV DISABLE_SANDBOXES="true"
ENV CDS_SANDBOX_URL="https://sandbox.cds-hooks.org"
ENV PICKER_CONFIG_R3="stu3-local"
ENV PICKER_ORIGIN="https://gt-apps.hdap.gatech.edu/smart-patientpicker"
ENV STU2_ENABLED="false"
ENV STU3_ENABLED="true"

#RUN cp -r /app /smart-launcher && mv /smart-launcher /app/smart-launcher

#COPY ./src/index.js /app/smart-launcher/src/index.js
#COPY ./src/index.js /app/src/index.js
#CMD ["node", "./smart-launcher/src/index.js"]