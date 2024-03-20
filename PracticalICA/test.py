from datetime import datetime
import hashlib 
import json
class BlockChain:

    def __init__(self):
        self.chain = []
        self.newTransaction = []

    def new_block(self,previousBlockHash, hash):
        newBlock = {
            'index': len(self.chain) + 1,
            'timestamp':datetime.now() ,
            'transaction': self.newTransaction,
            'proof': self.proof_of_work(),
            'hash': hash,
            'previousBlockHash': previousBlockHash
        }
        self.newTransaction = []
        self.chain.append(newBlock)
        return newBlock

    def last_block(self):
        return self.chain[-1]
    
    def create_new_transaction(self, a, s, r):
        new_trans = {
        'amount': a,
        'sender': s,
        'recipient': r
        }
        self.newTransaction.append(new_trans)
        return self.last_block()['index'] + 1
    
    def has(block):
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



