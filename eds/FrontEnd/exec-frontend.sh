#!/bin/sh
sh openmtc-gevent/run_gscl &
sleep 1
#until $(curl --output /dev/null --silent --head --fail http://localhost:6065/); do
#  printf '.'
#  sleep 1
#done
sh frontend
