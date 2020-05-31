from block import Block
class Blockchain:
    '''
    Blockchain is a public ledger of transactions
    Implemented as a list of blocks -- data sets of transaction
    '''
    def __init__(self):
        self.chain = [Block.genesis()]
    def add_block(self,data):
        self.chain.append(Block.mine_block(self.chain[-1],data))
    def __repr__(self):
        return 'Blockchain:{}'.format(self.chain)
def main_var():
    block_chain = Blockchain()
    block_chain.add_block('slesha')
    block_chain.add_block('mishra')
    print(block_chain)
if __name__ == "__main__":
    main_var()





