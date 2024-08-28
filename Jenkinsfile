ipeline {
    agent any
    
    stages {
        stage('Pipeline Artifact Directory Setting') {
            steps {
                sh 'echo directory setting'
                sh 'mkdir -p jenkins/artifact'
            }
        }
        stage('Requirement Analysis') {
            steps {
                sh 'echo requirement analysis'
                if (fileExists('jenkins/user_requirement.txt')){
                    sh 'python jenkins/analyze_req.py'           
                }
                else {
                    echo 'user_requirement.txt not found'
                }
            }
        }
        
        stage('ROS Node Integration') {
            steps {
                sh 'echo ros node inetgration'
                if (fileExists('jenkins/artifact/list_of_features.txt')){
                    sh 'python jenkins/integrate_node.py'
                }
                else {
                    echo 'list_of_features.txt not found'
                }
            }
        }
        
        stage('Container Packaging') {
            steps {
                if (fileExists('jenkins/artifact/list_of_nodes.yaml')){
                    sh 'echo container packaging'
                }
                else {
                    echo 'ist_of_nodes.yaml not found'
                }
            }
        }
        stage('Container Push') {
            steps {
                sh 'echo container push'
            }
        }
    }
    post {
        always {
            echo "Pipeline completed."
        }
    }
}