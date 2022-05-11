//SPDX-License-Identifier: Unlicense
pragma solidity 0.8.4;

import "hardhat/console.sol";

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract YelowToken is ERC20{

    address public owner;
    mapping(address => uint) public balances; 
    uint public totalsupplyOfTokens;
     

    constructor(uint _firstsupply) ERC20("Yelow","YLW") {
        owner = msg.sender;
        _mint(msg.sender, _firstsupply);
        totalsupplyOfTokens = _firstsupply;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "only owner");
        _;
    }

    function mintYelowTokens(address _user, uint _numberOfTokens) external {
        require(_user != address(0), "zero address supplied-not allowed");
        require(_numberOfTokens >0, "minimum 1 token is to be supplied for mint");
        super._mint(_user, _numberOfTokens);
        balances[msg.sender] = balances[msg.sender] +_numberOfTokens;
        totalsupplyOfTokens  = totalsupplyOfTokens + _numberOfTokens;
    }

    function burnYelowTokens(address _user, uint _numberOfTokens) external onlyOwner {
        require(_numberOfTokens >0, "minimum of 1 token is to be sent for burn");
        super._burn(_user, _numberOfTokens);
        balances[msg.sender] = balances[msg.sender] -_numberOfTokens;
        totalsupplyOfTokens = totalsupplyOfTokens - _numberOfTokens;
    }

    function getTotalYelowTokenSupply() public view returns (uint) {
        return totalsupplyOfTokens;
    }


}   