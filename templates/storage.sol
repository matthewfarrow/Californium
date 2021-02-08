//SPXD-License-Identifier: GPL-3.0
pragma solidity >= 0.4.16 < 0.8.0;


contract StoreValue {
    uint value;
    
    function set(uint x) public {
        value = x;
    }
    
    function get() public view returns (uint) {
        return value;
    }
    
} 


/*
Creator: Epicitius
*/