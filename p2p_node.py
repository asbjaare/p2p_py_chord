# p2p_node.py

import socket
import hashlib


# Consistant hash
def hash_function(key, size):
    return int(hashlib.sha1(key.encode("utf-8")).hexdigest(), 16) % size


def get_previous_node(ip, size):
    with open("ip.txt", "r") as f:
        entries = [line.strip().split(" - ") for line in f if " - " in line]
        ips = [entry[1] for entry in entries if len(entry) == 2]
        nodes = sorted((hash_function(ip, size), ip) for ip in ips)

    for i in range(len(nodes)):
        if nodes[i][1] == ip:
            if i == 0:
                return nodes[len(nodes) - 1][1]
            else:
                return nodes[i - 1][1]


# Chord node class
class ChordNode:
    def __init__(self, m=4):
        self.data = {}
        self.finger_table = []
        self.IP = socket.gethostbyname(socket.gethostname())
        self.size_of_cluster = 2**m
        self.node_id = hash_function(self.IP, self.size_of_cluster)
        self.key_size = m
        self.previous = hash_function(
            get_previous_node(self.IP, self.size_of_cluster), self.size_of_cluster
        )

    def __str__(self):
        return "Node ID: " + str(self.node_id)

    def finger_table(self):

        nodes = []

        with open("ip.txt", "r") as f:
            entries = [line.strip().split(" - ") for line in f if " - " in line]
            ips = [entry[1] for entry in entries if len(entry) == 2]
            nodes = sorted((hash_function(ip, self.size_of_cluster), ip) for ip in ips)

        for i in range(self.key_size):
            start = (self.node_id + 2**i) % self.size_of_cluster

            successor = next((id, ip) for id, ip in nodes if id >= start)
            if not successor:
                successor = nodes[0]
            self.finger_table.append((start, successor))

        print(self.finger_table)

        return self.finger_table

    # Rest of the ChordNode class implementation


# Rest of the Chord node code

if __name__ == "__main__":
    current_node = socket.gethostname()

    node = ChordNode()

    print(str(ChordNode()))
    ChordNode.finger_table(self=node)
    print("Previous node: " + str(node.previous))

    # app.run(host="0.0.0.0", port=8000)
