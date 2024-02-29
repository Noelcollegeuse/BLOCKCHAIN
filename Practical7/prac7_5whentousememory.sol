pragma solidity ^0.8.20;



contract Sum{
    // State variables are stored on the blockchain.

    function sumArray(uint[] memory array) public pure returns (uint) 
    {
        uint sum = 0;
        for (uint i = 0; i < array.length; i++)
        {
            sum += array[i];
        }
        return sum;
    }
}