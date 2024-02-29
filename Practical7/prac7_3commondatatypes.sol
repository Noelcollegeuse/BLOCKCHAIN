pragma solidity ^0.8.20;

contract Types{
    bool public valid = false;

    uint32 public uidata = 5012019; //un-signed integer
    int32 public idata = -6012019;

    uint32 public ui_data = 5_01_2019; //result will be same ==> 5012019
}