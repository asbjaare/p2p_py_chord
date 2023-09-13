#!/bin/sh

HOSTS=`cat /share/compute-nodes.txt`

for H in $HOSTS
do
	ssh -x $H "/bin/true" 2> /dev/null && echo $H &
done | sort -t "-" -k 1.2 -n -k 2 -n > hosts.txt

wait
