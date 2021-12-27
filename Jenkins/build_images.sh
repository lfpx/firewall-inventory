#!/bin/bash
# Login to Docker Hub using access token
docker login -u ${DOCKER_USERNAME} -p ${DOCKER_TOKEN}

build(){
export TAG="${1}"
echo -e "\n# Building container image <firewall-inventory:${TAG:-latest}>"
docker-compose -f Docker/docker-compose.yaml build

echo -e "\n# Pushing image <firewall-inventory:${TAG:-latest}> to registry"
docker-compose -f Docker/docker-compose.yaml push application
}

# Build and push image tagged <vYYYYMMDD-HHMM>
build v$(date '+%Y%m%d-%H%M')

# Build and push image tagged <latest>
build

docker logout

echo -e '\n# Removing images created more than 24h ago'
docker image prune --all --force --filter "until=24h"