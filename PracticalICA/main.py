



last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)

previous_hash = blockcahin.hash(last_block)
block = blockchian.new_block(proof,previous_hash)