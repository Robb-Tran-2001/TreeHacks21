import hashlib
import imagehash
from PIL import Image
from urllib import request
import numpy as np
import io
import time
import json

hashlist = []
dict = {}

def add_img(img_url):
  request.urlretrieve(img_url, "sample.jpg")
  img = Image.open("sample.jpg")
  img_byte_arr = io.BytesIO()
  img.save(img_byte_arr, format='PNG')
  img_byte_arr = img_byte_arr.getvalue()
  cs_div = hashlib.sha512(img_byte_arr).hexdigest()
  cs_con = imagehash.phash(Image.open('sample.jpg'))

  ts = str(time.time())
  block = {cs_div: ts}
  blockstring = cs_div + ts
  dict.update(block)
  if not hashlist:
    prev_hash = ""
  else:
    prev_hash = hashlist[-1]
  pre_new_hash = prev_hash + blockstring
  prep_new_hash = pre_new_hash.encode()
  new_hash = hashlib.sha512(prep_new_hash).hexdigest()
  hashlist.append(new_hash)

add_img("https://cdn.cnn.com/cnnnext/dam/assets/210107120929-elon-musk-mclaren-f1-1999-vault-large-169.jpg")
add_img("https://upload.wikimedia.org/wikipedia/commons/8/85/Elon_Musk_Royal_Society_%28crop1%29.jpg")
add_img("https://cdn.vox-cdn.com/thumbor/igbYazFaVO2_XZDhv0ARbAU93bM=/1400x1400/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19819160/1206292069.jpg.jpg")

print(hashlist)
print(dict)