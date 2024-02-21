function BlockChain(){
    this.chain=[];
    this.newTransaction=[];``
}

BlockChain.prototype.createNewBlock = function (nonce,previousBlockHash,hash){
    const newBlock={
        index:this.chain.length+1,
        timestamp:Date.now(),
        transaction:this.newTransaction,
        nonce:nonce,
        hash:hash,
        previousBlockHash:previousBlockHash,

    };
    this.newTransaction=[];
    this.chain.push(newBlock);
    return newBlock;
}

BlockChain.prototype.previousBlockHash=function(){
    return this.chain[this.chain.length-1].hash;
}

module.exports=BlockChain;