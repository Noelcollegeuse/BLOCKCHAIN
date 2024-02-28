var express = require("express");
var app = express();
var request = require("request");

request({
    url: "https://api.blockchain.info/stats?format=jason",
    jason: true
}, function(error,responce,body){
    btcPrice = body.market_price_usd;
    btcBlocks = body.n_blocks_total;
    btcFees = body.total_fees_btc;
    btcMined = body.n_blocks_mined;
    btcVolume = body.estimated_transaction_volume_usd;
});

app.get("/",function(req,res){
    res.send("Bitcoin Transaction Demo and Current Price is " +btcPrice );
});
app.get("/",function(req,res){
    res.send("\nBitcoin Transaction Demo and Block height is " +btcBlocks );
});
app.get("/",function(req,res){
    res.send("Bitcoin Transaction Demo and Fees is " +btcFees );
});
app.get("/",function(req,res){
    res.send("Bitcoin Transaction Demo and blocks mined is " +btcMined );
});
app.get("/",function(req,res){
    res.send("Bitcoin Transaction Demo and block volume is " +btcVolume );
});

app.listen(3000, function(){
    console.log("hello world");
})