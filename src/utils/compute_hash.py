import hashlib
 
class ComputeHash:
    @staticmethod
    def compute_hash(object):
        """
        Implement a SHA-256 hashing algorithm to generate a unique hash for each node
        """
        return hashlib.sha256(object.encode()).hexdigest()
