import hashlib
import json
import time

from src.utils import ComputeHash


class Block:
    def __init__(self, index, previous_hash, data, next_hash=None):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.next_hash = next_hash
        self.hash = ComputeHash.compute_hash(json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True))

    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:10]}, prev={self.previous_hash[:10]})"
