pragma solidity >0.5.99 <0.8.0;

contract Coin { 
    // The keyword "public" makes variables
    // accessible from other contracts
    address public minter;
    mapping (address => uint) public balances;
    bytes32 launch_hash = sha256(abi.encodePacked("oof"));

    // Events allow clients to react to specific
    // contract changes you declare
    event Sent(address from, address to, uint amount);
    
    event LaunchNukes();

    // Constructor code is only run when the contract
    // is created
    constructor() {
        minter = msg.sender;
    }

    // Sends an amount of newly created coins to an address
    // Can only be called by the contract creator
    function mint(address receiver, uint amount) public {
        require(msg.sender == minter);
        require(amount < 1e60);
        balances[receiver] += amount;
    }

    // Sends an amount of existing coins
    // from any caller to an address
    function send(address receiver, uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance.");
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        emit Sent(msg.sender, receiver, amount);
    }
    
    function authorizeNuclearLaunch(string memory code) public payable {
        require(msg.value >= 99 ether, "Not enough ether");

        if (sha256(abi.encodePacked(code)) == launch_hash) {
            emit LaunchNukes();
        }
    }
}
