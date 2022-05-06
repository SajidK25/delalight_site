#!/bin/bash
read -p "Do you really want to remove all existing containers, images, volumes and networks? Continue and remove all? (y/N) " decision
  if [ "$decision" != "Y" ] && [ "$decision" != "y" ]; then
    exit
  fi
docker-compose down
sleep 5
docker rmi $(docker images -q) -f
sleep 10
docker volume prune -f 
