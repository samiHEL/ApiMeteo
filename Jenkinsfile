pipeline {
    agent any

    stages {
        stage('Install Python Requests') {
            steps {
                // Utiliser un bloc de script pour exécuter des commandes shell
                script {
                    // Vérifie si pip est installé
                    sh 'python3 -m pip --version'
                    
                    // Installe le module requests
                    sh 'python3 -m pip install requests'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Exécute votre script Python après l'installation de requests
                    sh 'python3 apiMeteo.py'
                }
            }
        }
    }
}

