pipeline {
    agent any
    stages {
        stage('version') {
            steps {
              sh 'python3 --version'
            }
        }
        stage('hello') {
            steps {
              sh 'python3 hello.py'
            }
        }

        stage('Docker') {
            steps {
              sh 'sudo docker build .'
            }
        }
    }
}
