pragma solidity ^0.8.20;

contract ColorStorage
{
    mapping(address => string) private favoriteColors;

    function setFavoriteColor(string calldata color) public{
        favoriteColors[msg.sender] = color;
    }

    function getFavoriteColor(address userAddress) public view returns (string memory){
        return favoriteColors[userAddress];
    }
}