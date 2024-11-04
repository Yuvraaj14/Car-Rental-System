pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/Yuvraaj14/Car-Rental-System'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Use a shell command to install the dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Migrations') {
            steps {
                script {
                    // Run database migrations
                    sh 'python manage.py migrate'
                }
            }
        }

        stage('Collect Static') {
            steps {
                script {
                    // Collect static files
                    sh 'python manage.py collectstatic --noinput'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t truzzcarz .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run the Docker container
                    sh 'docker run -d -p 8000:8000 truzzcarz'
                    // Wait for the server to start
                    timeout(time: 30, unit: 'SECONDS') {
                        waitUntil {
                            script {
                                return sh(script: 'curl -f http://localhost:8000', returnStatus: true) == 0
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean workspace after the build
            cleanWs()
        }
        success {
            // Notify success (you can add email notifications or other actions here)
            echo 'Pipeline executed successfully!'
        }
        failure {
            // Notify failure
            echo 'Pipeline execution failed!'
        }
    }
}
