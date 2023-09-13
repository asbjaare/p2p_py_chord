HOSTS=$(cat /share/compute-nodes.txt)

# Create an empty file to store the results
> ip.txt

for H in $HOSTS
do
    # Use ping to get the IP address and discard other output
    IP=$(ping -c 1 $H | grep -oP '(\d+\.\d+\.\d+\.\d+)' | head -1)

    # Check if IP is not empty (host is reachable)
    if [ -n "$IP" ]; then
        echo "$H $IP" >> ip.txt
    fi
done

# Sort the results by IP address
sort -t "." -k 1,1n -k 2,2n -k 3,3n -k 4,4n -o ip.txt ip.txt
