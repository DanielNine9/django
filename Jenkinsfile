pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = "https://hub.docker.com"
        REPO_URL = "https://github.com/DanielNine9/django.git"
        BRANCH_NAME = "test"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${BRANCH_NAME}"]], userRemoteConfigs: [[url: "${REPO_URL}"]]])
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        
        stage('Run Tests') {
            steps {
                sh 'pip install -r requirements.txt' // Install dependencies
                sh 'python manage.py test' // Run tests
            }
        }

        stage('Build and Push Docker Image') {
            when {
                allOf {
                    branch 'main' // Only run this stage on the 'main' branch
                    not { changeset '.*' } // Only run if there are no changes since the last successful build
                }
            }
            steps {
                script {
                    def imageName = "${DOCKER_REGISTRY}/my_image_name:latest"
                    docker.build(imageName, './path_to_dockerfile') // Build Docker image from Dockerfile
                    docker.withRegistry("${DOCKER_REGISTRY}", 'docker_hub_credentials') {
                        docker.image(imageName).push() // Push the Docker image to the registry
                    }
                }
            }
        }
    }
}
