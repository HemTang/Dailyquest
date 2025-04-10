pipeline{
    agent any
    stages{
        stage('Build Image'){
            steps{
                echo "Building the Image from code/Dockerfile"
                sh 'docker-compose build'
            }
        }
        stage('Running Container'){
            steps{
                echo "Running Container"
                sh '''
                docker-compose down || true
                docker-compose up -d
                '''
            }
        }

        stage('Logs'){
            steps{
                echo "Displaying logs"
                sh 'cat logs/container.log || echo " No logs yet"'
            }
        }
        stage('Logs'){
            steps{
                echo "Displaying logs"
                sh 'cat logs/container.log || echo " No logs yet"'
            }
        }
        stage('Run Test'){
            steps{
                echo "Testing Endpoints"
                sh 'sleep 10'
                sh './test_app.sh'
            }
        }

    }
    post{
        success{
            echo "Build and deployent successful!"
        }
        failure{
            echo "Something went wrong!"
        }
    }
}