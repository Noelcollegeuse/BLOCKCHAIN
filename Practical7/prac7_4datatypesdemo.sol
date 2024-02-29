//Data types Demo 
pragma solidity ^0.8.20;

contract MyContract_2{
    enum State {waiting, ready, active}
    State public state;
    constructor() public {
        state = State.waiting;
    }
    function ready() public {
        state = State.ready;
    }
    function activate() public {
        state = State.active;
    }
    function isActive() public view returns(bool) {
        return state==State.active;
    }
    
}