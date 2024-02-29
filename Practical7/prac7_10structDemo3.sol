pragma solidity ^0.8.20;

contract MyContract {

    uint256 public peopleCount = 0;
    address public owner;
    modifier onlyOwner(){
        require(msg.sender == owner);
        _;
    }

    mapping(uint => Person) public people;
    constructor() public {
        owner=msg.sender;
    }
    struct Person {
        
        uint _id;
        string _firstName;
        string _lastName;
    }

    function addPerson(string memory _firstName, string memory _lastName) public onlyOwner{
        incrementCount();
        people[peopleCount] = Person(peopleCount, _firstName, _lastName);
    }

    function incrementCount() internal {
        peopleCount += 1;
    }
}