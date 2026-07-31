pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "Deploying Flask application..."
                    # Add your restart/deployment commands here (e.g., systemctl restart flask / gunicorn)
                '''
            }
        }
    }
}