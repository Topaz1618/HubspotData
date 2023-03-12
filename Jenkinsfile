pipeline {
    agent any
    stages {
        stage('Pull from GitHub') {
            steps {
                git 'https://github.com/Topaz1618/HubspotData.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building..."'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Testing..."'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying..."'
            }
        }
    }
}