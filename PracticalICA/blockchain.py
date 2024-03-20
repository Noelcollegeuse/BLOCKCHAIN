from time import time
import hashlib 
import json
class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash = '1',proof = 100)
    
    def new_block(self,proof,previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp':time() ,
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    def last_block(self):
        return self.chain[-1]
    
    def create_new_transaction(self, a, s, r):
        new_trans = {
        'amount': a,
        'sender': s,
        'recipient': r
        }
        self.current_transactions.append(new_trans)
        return self.last_block()
    
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





blockchian = BlockChain()
for i in range(2):
    numtrans = int(input("Enter the number of transactions: "))
    for j in range(numtrans):
        amount = float(input("Enter amount: "))
        sender = input("Enter sender: ")
        recipient = input("Enter recipient: ")
        blockchian.create_new_transaction(amount, sender, recipient)
    nonce = input("Enter nonce: ")
    hash = blockchian.hash(hash.chain[i])
    
    blockchian.new_block(1)


blockchian.create_new_transaction('alice','bob',1)
blockchian.create_new_transaction('alice','bob',2)
last_block = blockchian.last_block
#last_proof = last_block['proof']
#proof = blockchian.proof_of_work(last_proof)

#previous_hash = blockchian.hash(last_block)
#block = blockchian.new_block(proof,previous_hash)

print(blockchian.chain)
