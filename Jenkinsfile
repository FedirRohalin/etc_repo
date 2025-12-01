pipeline {
  options { timestamps()  }
  agent none
  stages {
    stage('Check scm') {
      agent any
      steps {
        checkout scm
      }
    }
    stage('Build') {
      steps {
        echo "Building...${BUILD_NUMBER}"
        echo 'Build complete'
      }
    }
    stage('Test') {
      agent {
        docker {
          image 'python:3.9-alpine'
          args '-u root'
        }
      }
      steps {
        sh 'apk add --no-cache build-base'
        sh 'pip install xmlrunner'
        sh 'mkdir -p test-reports'
        sh 'python3 tests.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
        success {
          echo 'Tests passed!'
        }
        failure {
          echo 'Tests failed!'
        }
      }
    }
  }
}
