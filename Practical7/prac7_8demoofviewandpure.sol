pragma solidity ^0.8.20;

contract ViewAndPure
{
    uint public x = 1;
    // Promise not to modify the state.
    function addToX(uint y) public view returns (uint) {
        return x + y;
    }

    //Promise not to modifty or read from the state.
    function add(uint i, uint j) public pure returns (uint){
        return i + j ;
    }
}