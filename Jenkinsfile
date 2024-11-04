pipeline {
    agent any 

    environment {
        // Set environment variables if needed, e.g., database credentials
        DATABASE_URL = 'sqlite:///db.sqlite3'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build the Docker image
                script {
                    def app = docker.build("truzzcarz:latest")
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests inside the Docker container
                script {
                    docker.image("truzzcarz:latest").inside {
                        sh 'python manage.py test'  // Replace with your actual test command
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application (adjust this step based on your deployment strategy)
                script {
                    // For example, push to a Docker registry
                    docker.withRegistry('https://your-docker-registry-url', 'your-credentials-id') {
                        docker.image("truzzcarz:latest").push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up
            cleanWs()
        }
        
        success {
            // Notify success (you can add email notifications or other actions here)
            echo 'Build and Deployment successful!'
        }
        
        failure {
            // Notify failure
            echo 'Build or Deployment failed!'
        }
    }
}
