# p2p_node.py

from flask import Flask, request
import hashlib
import os

app = Flask(__name__)

# The Chord ring size (e.g., 2^4 = 16 nodes)
RING_SIZE = 16

# Get the node ID from environment variable
node_id_str = os.environ.get("NODE_ID")

if node_id_str is not None:
    try:
        node_id = int(node_id_str)
    except ValueError:
        print("NODE_ID is not a valid integer.")
else:
    print("NODE_ID environment variable is not set.")
# Each node has an ID based on its ID
def get_node_id(node_id):
    return node_id % RING_SIZE


# Chord node class
class ChordNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.data = {}

    # Rest of the ChordNode class implementation


# Rest of the Chord node code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
