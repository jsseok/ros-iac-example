pipeline {
    agent any
    
    stages {
        stage('Pipeline Artifact Directory Setting') {
            steps {
                echo 'directory setting'
                sh 'mkdir -p jenkins/artifact'
                sh 'pip install -r jenkins/requirements.txt'
            }
        }
        stage('Requirement Analysis') {
            steps {
                echo 'requirement analysis'
                script {
                    if (fileExists('jenkins/user_requirement.txt')) {
                        sh 'python3 jenkins/analyze_req.py'           
                    } else {
                        echo 'user_requirement.txt not found'
                    }
                }
            }
        }
        stage('ROS Node Integration') {
            steps {
                echo 'ros node inetgration'
                script {
                    if (fileExists('jenkins/artifact/list_of_features.txt')) {
                        sh 'python3 jenkins/integrate_node.py'
                    } else {
                        echo 'list_of_features.txt not found'
                    }
                }
            }
        }
        stage('Container Packaging') {
            steps {
                echo 'container packaging'
                script {
                    if (fileExists('jenkins/artifact/list_of_nodes.yaml')) {
                        echo 'execute some commands'
                    } else {
                        echo 'list_of_nodes.yaml not found'
                    }
                }
            }
        }
        stage('Container Push') {
            steps {
                echo 'container push'
            }
        }
    }
    post {
        always {
            echo "Pipeline completed."
        }
    }
}