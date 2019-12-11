#!/bin/bash

pkill redis-server
brew services restart redis
sleep 3
redis-server &

cd /Users/student/Desktop/redis

for folder in 7000 7001 7002 7003 7004 7005 7006
do
  rm -rf ${folder}
done

sleep 1

for port in 7000 7001 7002 7003 7004 7005
do
  mkdir ${port}
  cd ${port}
  cat >redis.conf << EOF
port ${port}
cluster-announce-ip 10.0.89.7
cluster-announce-port ${port}
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
appendonly yes
protected-mode no

dir ./
loglevel notice
logfile ${port}.log

save 900 1
save 300 10
save 60 10000
EOF
  sleep 1
  redis-server ./redis.conf &
  cd ..
done
sleep 1

redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1


# cd Desktop/redis/700
# redis-server ./redis.conf
# redis-cli --cluster create 127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 --cluster-replicas 1