// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Variables{
    // State variables are stored on the blockchain.
    string public text = "hello";
    uint public num = 123;

    function doSomething() view public 
    {
        //Local variable are not saved to the blockchain.

        uint i = 456;
        
        // Here are some global variables
        uint timestamp = block.timestamp; //Current bloick timestamp
        address sender = msg.sender; // address of the caller

    }
}