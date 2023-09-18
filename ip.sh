#!/bin/sh

# EXCLUDE="c2-11 c3-41"
EXCLUDE=""

HOSTS=`cat /share/compute-nodes.txt`

for H in $EXCLUDE
do
    HOSTS=`echo $HOSTS | sed -e "s/${H}//"`
done

for H in $HOSTS
do
    # Use ping to get the IP address and discard other output
    IP=$(ping -c 1 $H | grep -oP '(\d+\.\d+\.\d+\.\d+)' | head -1)

    # Check if IP is not empty (host is reachable)
    if [ -n "$IP" ]; then
        echo "$H - $IP"
    fi
done | sort -t "." -k 1,1n -k 2,2n -k 3,3n -k 4,4n > ip.txt

wait
