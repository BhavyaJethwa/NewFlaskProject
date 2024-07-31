pipeline {
agent any





stages {
    stage('Build') {
        steps {
            // Get some code from a GitHub repository
            git url: 'https://github.com/BhavyaJethwa/NewFlaskProject.git'

            // Run Maven on a Unix agent.
            script{
            if(isUnix()){
            sh "pip install -r requirements.txt"
            }
            else{
            bat "pip install -r requirements.txt"
            }
            }
        }
        }



    stage('Unit Test') {
        steps {

            // Run Maven on a Unix agent.
            script{
            if(isUnix()){
            sh "pytest"
            }
            else{
            bat "pytest"
            }
            }
        }

    }
    stage('Docker Build') {
            steps {
                script{
                if(isUnix()){
                sh "docker build -t bhavyadocker11/newflaskappjenkins  ."
                }
                else{
                 bat "docker build -t bhavyadocker11/newflaskappjenkins ."
                 }
                 }

            }
        }
    stage('Docker Push') {
            steps {
               withCredentials([usernamePassword(credentialsId:'dockerHub',passwordVariable: 'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                bat "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                bat "docker push bhavyadocker11/newflaskappjenkins:latest"
                }
    stage('Kubernetes Pod') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f deployment.yaml"
 } else {
 bat("kubectl apply -f deployment.yaml")
 }
                }
    }

 }

 stage('Kubernetes Service') {

    steps {
                script{
 if (isUnix()){

 sh "kubectl apply -f service.yaml"
 } else {
 bat("kubectl apply -f service.yaml")
 }
                }
    }

 }

    }

            }
    }
}
}