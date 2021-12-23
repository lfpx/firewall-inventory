#!/bin/bash
echo '# Building container image'
IMAGE_NAME=firewall-inventory
TAG=v$(date '+%Y%m%d-%H%M')
docker build -t "${DOCKER_USERNAME}"/"${IMAGE_NAME}":"${TAG}" \
              -t "${DOCKER_USERNAME}"/"${IMAGE_NAME}":latest -f Docker/Dockerfile .
if [[ $(docker images "${DOCKER_USERNAME}"/"${IMAGE_NAME}":"${TAG}" -q | wc -l) -eq 0 ]]; then
    echo "# Error building image <${IMAGE_NAME}:${TAG}>"
    return 1
fi
echo '# Pushing images to registry'
docker login -u ${DOCKER_USERNAME} -p ${DOCKER_TOKEN}
docker push "${DOCKER_USERNAME}"/"${IMAGE_NAME}":"${TAG}"
docker push "${DOCKER_USERNAME}"/"${IMAGE_NAME}":latest
docker logout

echo '# Removing local images'
docker rmi "${DOCKER_USERNAME}"/"${IMAGE_NAME}":"${TAG}"
docker rmi "${DOCKER_USERNAME}"/"${IMAGE_NAME}":latest