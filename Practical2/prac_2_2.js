const prompt=require('prompt-sync')();
const Blockchain = require('./prac_2_1')
var bitcoin = new Blockchain;
bitcoin.createNewBlock(123,'genesis','block1');
var nonce;
var hash;
var phase;
var transactions;
noofblock = prompt("Enter No of Blocks :"); 

    
    for( var i=1;i<=noofblock;i++)
        {
        transactions = prompt("Enter No of Transaction :"); 
        nonce = prompt("Enter Nonce :");
        hash = prompt("Enter hash : ");
        phase = bitcoin.previousBlockHash();
        

        for(var j=0;j<transactions;j++){   
            amount = prompt("Enter amount :");
            sender = prompt("Enter sender :");
            recipent = prompt("Enter recipent :");     
            bitcoin.createNewTransaction(amount,sender,recipent);
            
        }
        bitcoin.createNewBlock(nonce,phase,hash);
     
        }
    

console.info(JSON.stringify(bitcoin, null, "  "));