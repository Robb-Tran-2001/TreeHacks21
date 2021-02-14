import hashlib
from time import time
import imagehash
from PIL import Image
from urllib import request
import numpy as np
import io
import json

class Block:
  def __init__(self, index, nonce, previous_hash, img_path, genesis=False):

    self.timestamp = time()
    self.index = index
    self.nonce = nonce
    self.previous_hash = previous_hash

    if genesis:
      self.hash = ['0' * 512][0]
      self.cs_div = None
      self.cs_con = None
      return

    cs_div, cs_con = self.get_checksums(img_path)

    self.cs_div = cs_div
    self.cs_con = str(cs_con)

    self.hash = self.hash_block((str(self.timestamp) + self.cs_div + str(self.cs_con)).encode('utf-8'))

    # self.data = {
    #   str(cs_con): cs_div
    # }

  def get_timestamp(self):
    return self.timestamp

  def hash_block(self, text):
    return hashlib.sha512(text)
  
  def get_checksums(self, img_path):
    #request.urlretrieve(img_path, "sample.jpg")

    if img_path == "":
      raise Exception("Empty image filepath not allowed")

    img = Image.open(img_path)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    cs_div = hashlib.sha512(img_byte_arr).hexdigest()
    cs_con = imagehash.phash(Image.open(img_path))

    return cs_div, cs_con
