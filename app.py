# app1.py
from flask import Flask
import sys
import hashlib
import socket
from config import KEY_SIZE, CLUSTER_SIZE


def hash_function(key):
    return int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % CLUSTER_SIZE


def get_previous_ip(ip):
    with open("ip.txt", "r") as f:
        entries = [line.strip().split(" ") for line in f if " " in line]
        ips = [entry[1] for entry in entries if len(entry) == 2]
        nodes = sorted((hash_function(ip), ip) for ip in ips)

    for i in range(len(nodes)):
        if nodes[i][1] == ip:
            if i == 0:
                return nodes[len(nodes) - 1][1]
            else:
                return nodes[i - 1][1]


def populate_fingertable(host_ip, node_id):
    nodes = []
    finger_table = []
    with open("ip.txt", "r") as f:
        entries = [line.strip().split(" ") for line in f if " " in line]
        ips = [entry[1] for entry in entries if len(entry) == 2]
        nodes = sorted((hash_function(ip), ip) for ip in ips)
    for i in range(KEY_SIZE):
        start = (node_id + 2**i) % CLUSTER_SIZE

        successor = next((id, ip) for id, ip in nodes if id >= start)
        if not successor:
            successor = nodes[0]
        finger_table.append((start, successor))

    return finger_table


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from App 1!"


@app.get("/item/<key>")
def item_get(key):
    print(finger_table)
    # TODO: make it look for the item, for now we just se if we have it and if not we ask the next node
    # TODO: use fingertables instead of just asking the next node
    #
    print(data)
    if key in data:
        return f"key is data {key}"
    else:
        return f"key is not data {data}"


@app.put("/item/<key>")
def item_put(key):
    # TODO: calculate the position of the item based upon its hash, and if we can't store it ourself
    # send it to the next node

    # TODO: use fingertables instead of just asking the next node
    prev_node = hash_function(prev_node_ip)

    # calculate the range
    if prev_node < node_id:
        if prev_node < key <= node_id:
            # its ourself
            pass
        else:
            # go to fingertables
            pass
    else:
        if key <= node_id or prev_node < key:
            # its ourself
            pass
        else:
            # go to fingertables
            pass

    data.append(key)

    return f"OK {data}"


@app.route("/neighbours")
def neighbours_get():
    return "neighbours"


@app.route("/kill/all")
def kill():
    # TODO: send kill signal to next node and kill the flask application

    sys.exit(1)


if __name__ == "__main__":
    # prev_node_ip = sys.argv[1]
    # next_node_ip = sys.argv[2]

    data = []
    host_ip = socket.gethostbyname(socket.gethostname())
    node_id = hash_function(host_ip)
    print(node_id)

    prev_node_ip = get_previous_ip(host_ip)
    print(prev_node_ip)
    print(hash_function(prev_node_ip))
    finger_table = populate_fingertable(host_ip, node_id)

    app.run(host="0.0.0.0", port=65000)
