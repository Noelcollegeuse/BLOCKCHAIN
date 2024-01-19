const prompt=require('prompt-sync')();
const Blockchain = require('./prac_1_1')
var bitcoin = new Blockchain;
bitcoin.createNewBlock(123,'genesis','block1');
var nonce;
var hash;
var phase;
for(var i=0;i<3;i++)
{
    nonce = prompt("Enter Nonce :");
    hash = prompt("Enter hash : ");
    phase = bitcoin.previousBlockHash();
    bitcoin.createNewBlock(nonce,phase,hash);
}

console.log(bitcoin);