import hashlib
from block import Block

class Blockchain:
  def __init__(self):
    self.__current_media = []
    self.__chain = []

    self.create_genesis()
  
  @property
  def last_block(self):
      return self.__chain[-1]

  @property
  def full_chain(self):
      return self.__chain
  
  def create_genesis(self):
    genesis_block = Block(0, 0, '00', "")
    self.__chain.append(genesis_block)

  @staticmethod
  def validate_proof_of_work(last_nonce, last_hash, nonce):
      """
      Validates the nonce
      :param last_nonce: <int> Nonce of the last block
      :param nonce: <int> Current nonce to be validated
      :param last_hash: <str> Hash of the last block
      :return: <bool> True if correct, False if not.
      """
      sha = hashlib.sha256(f'{last_nonce}{last_hash}{nonce}'.encode())
      return sha.hexdigest()[:4] == '0000'

  def generate_proof_of_work(self, block):
      """
      Very simple proof of work algorithm:
      - Find a number 'p' such that hash(pp') contains 4 leading zeroes
      - Where p is the previous proof, and p' is the new proof
      :param block: <Block> reference to the last block object
      :return: <int> generated nonce
      """
      last_nonce = block.nonce
      last_hash = block.hash

      nonce = 0
      while not self.validate_proof_of_work(last_nonce, last_hash, nonce):
          nonce += 1

      return nonce

  def add_block(self, block):
    self.__chain.append(block)
    self.__current_media = []

  def register_img(self, img_path):
    last_block = self.last_block
    index = last_block.index + 1
    previous_hash = last_block.hash

    # Let's start with the heavy duty, generating the proof of work
    nonce = self.generate_proof_of_work(last_block)

    block = Block(index, nonce, previous_hash, img_path)

    self.add_block(block)
  


