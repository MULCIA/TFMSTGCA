docker rm $(docker ps -a | grep tfm)
docker rmi $(docker images | grep tfm)
