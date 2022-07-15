pipeline {
   agent any
   stages {
    stage('Pull Code') {
      steps {
checkout([$class: 'GitSCM', branches: [[name: '*/master']],
    userRemoteConfigs: [[url: 'https://github.com/avishai0528/devops-project02.git']]])
          }
       }
    }
  }
}
