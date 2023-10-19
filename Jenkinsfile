pipeline {
    agent any
    stages {
        stage('version') {
            steps {
              sh 'python3 --version'
            }
        }
        stage('Docker') {
            steps {
              sh 'docker-compose up --build .'
            }
        }
    }
}
