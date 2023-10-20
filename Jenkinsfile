pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-vikash')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t vikash077/flask_docker:latest ."
                }
            }
        }
        stage('login to dockerhub'){
          steps{
            sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker loing -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin}"
          }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "docker push vikash077/flask_docker:latest"
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully.'
        }
    }
}
