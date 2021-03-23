pipeline {
    environment {
        NAME = 'ledshim'
        VERSION = 'latest'
        REGISTRY = 'bartbrinkman/homelab-ledshim'
        REGISTRY_CREDENTIALS = 'Dockerhub'
    }
    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build.yaml'
        }
    }
    stages {
        stage('Build') {
            steps {
                container('docker') {
                    sh "docker build --cache-from ${REGISTRY}:${VERSION} -t ${REGISTRY}:${VERSION} ."
                }
            }
        }
        stage('Publish') {
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIALS}", url: ""]) {
                        sh "docker push ${REGISTRY}:${VERSION}"
                    }
                }
            }
        }
    }
}