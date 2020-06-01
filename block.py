import time

from crypto_hash import crypto_hash

class Block:
    '''
    Block is a storage unit of storage
    It stores transactions in a blockchain that helps us with making it a crypto currency
    blocks have - Timestamp, last_hash (hash for last block), data, hash(for the this block)
    '''
    def __init__(self,time_stamp,last_hash,hash,data):
        self.data = data
        self.time_stamp = time_stamp
        self.hash = hash
        self.last_hash = last_hash
    def __repr__(self):
        return 'Block :\n time_stamp: {} \n last_hash: {}\n hash: {} \n data: {}'.format(self.time_stamp,self.last_hash,
                                                                                    self.hash,self.data)
    @staticmethod
    def mine_block(last_block, data):
        '''
       Will mine a block
        '''
        time_stamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(time_stamp,last_hash,data)

        return Block(time_stamp, last_hash, hash, data)
    @staticmethod
    def genesis():
        '''
        The genesis block is the block is a block that is a hard coded
        It does signify the first block in the series of block chains
        this will return a block instance
        '''
        return Block(1, 'genesis_last_hash', 'genesis_hash', [])
def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block,'foo')
    print(block)

if __name__ == '__main__':
    main()


