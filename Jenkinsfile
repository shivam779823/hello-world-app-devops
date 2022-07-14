


pipeline {
    agent any
    environment {
        PROJECT_ID = ' qwiklabs-gcp-04-6967b1341be1'
        CLUSTER_NAME = 'jenkins-cd'
        LOCATION = 'us-central1-a'
        CREDENTIALS_ID = 'kubernetes'
        dockerImage = "hello-world-python"
    }
    stages {
        stage("Checkout code") {
            steps {
              git branch: 'main', url: 'https://github.com/shivam779823/hello-world-app-devops.git'  
            }
        }
        stage("Build image") {
            steps {
                script {
                    dockerImage = docker.build("shiva9921/hello-world-python")
                }
            }
        }
        stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhublogin') {
                            dockerImage.push("latest")
                           
                    }
                }
            }
        }        
        stage('Deploy to GKE') {
            steps{

	
				echo "Start deployment of deployment.yaml"
				step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
			   
                echo "Start deployment of service.yaml"
			    step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'service.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
               
                echo "Deployment Finished ..."

            }
        }
    }    
}

