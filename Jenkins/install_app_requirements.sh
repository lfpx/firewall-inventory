#!/bin/bash
echo '# Installing Python packages: venv, pip'
sudo apt update
sudo apt install -y python3-venv python3-pip

echo '# Creating Python virtual environment .env'
python3 -m venv .venv

echo '# Activating virtual environment .env'
source .venv/bin/activate

echo '# Installing modules from requirements.txt'
python3 -m pip install -r requirements.txt