#!/bin/bash
export $(cat .env) > /dev/null 2>&1; 
docker stack deploy -c docker-compose.yaml ${1:-STACK_NAME}