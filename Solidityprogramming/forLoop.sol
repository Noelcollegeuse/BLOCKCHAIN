pragma solidity ^0.8.20;
contract ForLoop{
uint256[] data;
function loop() public returns (uint256[] memory){
for(uint256 i = 0; i <5; i++){
data.push(i);
}
return data;
}
}