from datetime import datetime
import hashlib 
import json
class BlockChain:

    def __init__(self):
        self.chain = list()
        self.current_transactions = []

    def new_block(self,previousBlockHash):
        newBlock = {
            'index': len(self.chain) + 1,
            'timestamp':datetime.now() ,
            'transaction': self.current_transactions,
            'proof': proof,
            'previousBlockHash': previousBlockHash
        }
        self.current_transactions = []
        self.chain.append(newBlock)
        return newBlock

    def last_block(self):
        return self.chain[:-1]
    
    def create_new_transaction(self, a, s, r):
        new_trans = {
        'amount': a,
        'sender': s,
        'recipient': r
        }
        self.current_transactions.append(new_trans)
        return self.last_block()['index'] + 1
    
    def hash(block):
        block_string = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self,last_proof):
        proof = 0
        while self.valid_proof(last_proof,proof) is False:
            proof +=1
        return proof
    def valid_proof(last_proof,proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4]=="0000"

last_block = BlockChain.last_block
last_proof = last_block('proof')
proof = BlockChain.proof_of_work(last_proof)

previous_hash = BlockChain.hash(last_block)
block = BlockChain.new_block(proof,previous_hash)

print(block)
