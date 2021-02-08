// SPDX-License-Identifier: GPL-3.0
pragma solidity >0.5.99 <0.8.0;

contract Coin {
    //create address that is pubically visible
    adress public minter;
    
    //maps the balance to the adress in a dictionary
    mapping (address => uint) public balances;
    
    //event allows people to see and react to action
    event Sent(address from, address to, uint amount)
    
    constructor() {
        minter = msg.sender;
    }
}