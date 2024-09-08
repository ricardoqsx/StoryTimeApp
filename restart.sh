#!/bin/bash

docker compose down
rm -rf dbdata/
docker system prune -a -f
docker compose up -d