import hashlib as hasher
import datetime as date
import time
from network import data

class Block:
    def __init__(self, index, timestamp, data, perv_has):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = perv_has
        self.hash = self.hash_block()
    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') + str(self.data).encode('utf-8')
                   + str(self.prev_hash).encode('utf-8'))
        return sha.hexdigest()
def create_genesis_block():
    return Block(0, date.datetime.now(), "Gen Block", "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = str(data) + " " + str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)


if __name__ == '__main__':
    print("Creating Blockchain!\n")
    blockchain = [create_genesis_block()]
    prev_block = blockchain[0]

    num_block=len(data)

    for i in  range(num_block):
        block_to_add = next_block(prev_block, data[i])
        blockchain.append(prev_block)
        prev_block = block_to_add
        time.sleep(2)
        print("Block #{} has been added\n".format(block_to_add.index))
        print("Block data: {}\n".format(block_to_add.data))
        print("Hash: {}\n".format(block_to_add.hash))
        print("*************************************************************************\n")
