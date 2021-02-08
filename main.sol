pragma solidity >0.5.99 <0.8.0;

contract Californium {
    // Track how many tokens are owned by each address.
    mapping (address => uint256) public balanceOf;

    // Modify this section
    string public name = "Californium";
    string public symbol = "CAL";
    uint8 public decimals = 16;
    uint256 public totalSupply = 1000 * (uint256(1) ** decimals);
    bytes32 launch_hash = sha256(abi.encodePacked("oof"));
    
    event LaunchNukes();
    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor() public{
        // Initially assign all tokens to the contract's creator.
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint256 value) public returns (bool success) {
        require(balanceOf[msg.sender] >= value);

        balanceOf[msg.sender] -= value;  // deduct from sender's balance
        balanceOf[to] += value;          // add to recipient's balance
        emit Transfer(msg.sender, to, value);
        return true;
    }
    
    function authorizeNuclearLaunch(string memory code) public payable {
        require(msg.value >= 99 ether, "Not enough ether");

        if (sha256(abi.encodePacked(code)) == launch_hash) {
            emit LaunchNukes();
        }
    }
}
