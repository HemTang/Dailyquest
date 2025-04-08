pipeline{
    agent any
    stages{
        stage('Build container'){
            steps{
                echo "Building the app"
                sh 'docker-compose build'
            }
        }
        stage('Running Container'){
            steps{
                echo "Running Container"
                sh 'docker-compose up -d'
            }
        }
        stage('Deploy application'){
            steps{
                echo "Deploying application to check if it works"
                
            }
        }

    }





}