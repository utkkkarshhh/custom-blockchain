import hashlib
import json
import time


class Block:
    def __init__(self, index, previous_hash, data, next_hash=None):
        self.index = index
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.data = data
        self.next_hash = next_hash
        self.hash = self.compute_hash()
    
    def compute_hash(self):
        """
        Implement a SHA-256 hashing algorithm to generate a unique hash for each node
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
        }, sort_keys=True)
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def __repr__(self):
        return f"Block(index={self.index}, hash={self.hash[:10]}, prev={self.previous_hash[:10]})"

    