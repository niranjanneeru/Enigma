#!/bin/bash

sudo docker-compose -f production.yml down
git pull
sudo docker-compose -f production.yml build
sudo docker-compose -f production.yml up -d
