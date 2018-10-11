#!/usr/bin/env groovy
pipeline{
    agent any

    //Define stages for the build process
    stages{
        //Define the deploy stage
        stage('Deploy'){
            steps{
                script{
                    docker.withRegistry('https://gt-build.hdap.gatech.edu'){
                        //Build and push the database image
                        def smartFhirImage = docker.build("smartfhir:1.0", "-f ./smart-fhir/Dockerfile ./smart-fhir")
                        smartFhirImage.push('latest')

                        //Build and push the database image
                        def smartMysqlImage = docker.build("smartmysql:1.0", "-f ./smart-mysql/Dockerfile ./smart-mysql")
                        smartMysqlImage.push('latest')

                        //Build and push the database image
                        def smartOauthImage = docker.build("smartoauth:1.0", "-f ./smart-oauth/Dockerfile ./smart-oauth")
                        smartOauthImage.push('latest')

                        //Build and push the database image
                        def smartPatientPickerImage = docker.build("smartpatientpicker:1.0", "-f ./smart-patientpicker/Dockerfile ./smart-patientpicker")
                        smartPatientPickerImage.push('latest')

                        //Build and push the database image
                        def smartPostgresqlImage = docker.build("smartpostgresql:1.0", "-f ./smart-postgresql/Dockerfile ./smart-postgresql")
                        smartPostgresqlImage.push('latest')

                        //Build and push the database image
                        def smartPythonAppImage = docker.build("smartpythonapp:1.0", "-f ./smart-pythonapp/Dockerfile ./smart-pythonapp")
                        smartPythonImageApp.push('latest')
                    }
                }
            }
        }

        //Define stage to notify rancher
        stage('Notify'){
            steps{
                script{
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartfhir:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-fhir', timeout: 60
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartmysql:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-mysql', timeout: 60
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartoauth:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-oauth', timeout: 60
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartpatientpicker:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-patientpicker', timeout: 60
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartpostgresql:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-postgresql', timeout: 60
                    rancher confirm: true, credentialId: 'gt-rancher-server', endpoint: 'https://gt-rancher.hdap.gatech.edu/v2-beta', environmentId: '1a7', environments: '', image: 'gt-build.hdap.gatech.edu/smartpythonapp:latest', ports: '', service: 'HDAP-SMARTonFHIR/smart-pythonapp', timeout: 60
                }
            }
        }
    }
}