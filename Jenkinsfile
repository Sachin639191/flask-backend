pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/usr/bin:/bin"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sachin639191/flask-backend.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    /home/ubuntu/venv/bin/python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    sudo -u ubuntu pm2 restart flask-backend || sudo -u ubuntu pm2 start app.py --name "flask-backend" --interpreter /home/ubuntu/venv/bin/python3
                '''
            }
        }
    }

    post {
        success {
            echo 'Flask app deployed successfully!'
        }
        failure {
            echo 'Flask deployment failed!'
        }
    }
}
