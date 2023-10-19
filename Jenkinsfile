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
                    // Define your Docker image name and tag
                    def dockerImageName = 'vikash077/flask_docker'
                    def dockerImageTag = "${BUILD_NUMBER}"

                    // Build the Docker image
                    sh "docker build -t ${dockerImageName}:${dockerImageTag} ."
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
                    // Log in to Docker Hub with your credentials
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIALS, usernameVariable: 'vikash007', passwordVariable: 'Vikash007@')]) {
                        sh "docker login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}"
                    }

                    // Push the Docker image to Docker Hub
                    def dockerImageName = 'vikash077/flask_docker'
                    def dockerImageTag = "${BUILD_NUMBER}"
                    sh "docker push ${dockerImageName}:${dockerImageTag}"
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

