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

    if genesis:
      self.hash = ['0' * 512][0]
      self.data = {
        None: None
      }
      return

    cs_div, cs_con = self.get_checksums(img_path)

    self.hash = self.hash_block((str(self.timestamp) + cs_div + str(cs_con)).encode('utf-8'))

    self.data = {
      cs_con: cs_div
    }

  def get_timestamp(self):
    return self.timestamp

  def hash_block(self, text):
    return hashlib.sha512(text)
  
  def get_checksums(self, img_path):
    #request.urlretrieve(img_path, "sample.jpg")

    if img_path == "":
      return None, None

    img = Image.open("sample.jpg")
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    cs_div = hashlib.sha512(img_byte_arr).hexdigest()
    cs_con = imagehash.phash(Image.open('sample.jpg'))

    return cs_div, cs_con
