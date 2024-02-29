//Solidity program to demonstarate how to write a smart contract 
pragma solidity ^0.8.20;
//Defining a contract
contract Storage
{
    //Declaring state variable 
    uint public setData;
    //Defining public function that sets the value of the state variable
    function set(uint x )public
    {
        setData = x;
    }
    //Defining function to print the value of state variable 
    function get()
    public view returns (uint)
    {
        return setData;
    }
}