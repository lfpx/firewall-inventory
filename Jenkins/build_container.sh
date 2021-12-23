#!/bin/bash
echo '# Building container'
docker build -t firewall-inventory:latest -f Docker/Dockerfile .
