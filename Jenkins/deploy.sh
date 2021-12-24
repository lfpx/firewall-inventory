#!/bin/bash
echo '# Copying docker_compose.yaml to deployment server'
scp ./run_app.sh ../Docker/docker-compose.yaml ${DEPLOYMENT_SERVER}:${DEPLOYMENT_PATH}

echo '# Starting app on remote server'
ssh ${DEPLOYMENT_SERVER} source ${DEPLOYMENT_PATH}/run_app.sh firewall-inventory
