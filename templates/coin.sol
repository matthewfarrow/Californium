//SPDX license identifier
pragma solidity >0.5.99 <0.8.0;

contract Coin {
    
    address public minter;
    mapping (address => uint) public balances;
    
    event Sent(address from, address to, uint amount);
    
    constructor() {
        minter = msg.sender;
    }
    
    function mint(address reciver, uint amount) public {
        require(msg.sender == minter);
        require(amount < 1e8);
        balances[reciver] += amount;
    }
    
    function Send(address reciver, uint amount) public {
        require(amount < balances[msg.sender]);
        balances[msg.sender] -= amount;
        balances[reciver] += amount;
        emit Sent(msg.sender, reciver, amount);
    }
}