import hashlib
from time import time

class Block:
  def __init__(self, index, nonce, previous_hash, img_path):
    self.timestamp = time()
    self.index = index
    self.nonce = nonce
    self.hash = self.hash_block(img_path)
  
  def hash_block(self, img_path):
    if img_path == "":
      return "1"

    with open(img_path,"rb") as f:
      bytes = f.read() # read entire file as bytes
      readable_hash = hashlib.sha256(bytes).hexdigest();
      print(readable_hash) 
      return readable_hash
