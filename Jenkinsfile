pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/avishai0528/devops-project02.git'
            }
        }    
        stage('run rest_app.py') {
            steps {
                bat 'start /min python rest_app.py'
            }
        }
        stage('run web_app.py') {
            steps {
                bat 'start /min python web_app.py'
            }
        }
        stage('run backend_testing.py') {
            steps {
                bat 'pip install requests'
                bat 'python backend_testing.py'
            }
        }
        stage('run frontend_testing.py') {
            steps {
                bat 'python frontend_testing.py'
            }
        }
        stage('run combined_testing.py') {
            steps {
                bat 'python combined_testing.py'
            }
        }
        stage('run clean_environment.py') {
            steps {
                bat 'python clean_environment.py'
            }
        }
    }
}
