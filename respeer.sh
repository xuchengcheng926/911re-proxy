#!/bin/bash
docker stop `docker ps -aq`
cd /root/peer2profit
docker-compose start 
cd /root/peer2
docker-compose start
cd /root/peer3
docker-compose start  p2p1
docker ps -aq
