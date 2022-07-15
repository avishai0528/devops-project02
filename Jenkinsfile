pipeline {
   agent any
   stages {
    stage('Pull Code') {
      steps {
        script {
           git url: 'https://github.com/aakashsehgal/FMU.git'
           sh "ls -lart ./*" 
           sh "git branch -a"
           sh "git checkout branchname"
          }
       }
    }
  }
}
