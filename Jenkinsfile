pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t vikash077/flask_jenkinss ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                }
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
