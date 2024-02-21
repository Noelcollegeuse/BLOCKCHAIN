function BlockChain(){
    this.chain=[];
    this.newTransaction=[];
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
BlockChain.prototype.getlastBlock=function() {
    return this.chain[this.chain.length - 1];
}
BlockChain.prototype.previousBlockHash=function(){
    return this.chain[this.chain.length-1].hash;
}
BlockChain.prototype.createNewTransaction=function(a,s,r)
{
    const newTrans={
        amount:a,
        sender:s,
        recipient:r
    };
    this.newTransaction.push(newTrans);

    return this.getlastBlock()['index']+1;
}

module.exports=BlockChain;
