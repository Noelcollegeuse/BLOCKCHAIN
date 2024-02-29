pragma solidity ^0.8.20;



contract Calldatatype{
    // When to use Calldata
    function isOwner(address ownerAddress) public view returns (bool)
    {
        return ownerAddress == msg.sender;
    }

 
}