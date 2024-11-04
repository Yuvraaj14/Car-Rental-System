pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Yuvraaj14/Car-Rental-System'
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

        stage('Start Django Server') {
            steps {
                script {
                    // Start the Django server in the background
                    sh 'nohup python manage.py runserver 0.0.0.0:8000 &'
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
