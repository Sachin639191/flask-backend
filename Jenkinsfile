pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_GITHUB_USERNAME/flask-backend.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    pm2 delete flask-app || true
                    pm2 start "venv/bin/python app.py" --name flask-app
                    pm2 save
                '''
            }
        }
    }
}