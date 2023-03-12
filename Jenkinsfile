pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/Topaz1618/HubspotData.git', branch: 'master'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t myapp .'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run --rm myapp pytest'
      }
    }
    stage('Deploy') {
      steps {
        sh 'docker-compose up -d'
      }
    }
  }
}
