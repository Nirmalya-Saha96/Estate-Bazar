pragma solidity ^0.8.11;

contract Factory {
    address[] public deploy;

    function buy (
        string calldata clientId,
        string calldata propertyId,
        uint256  value
    ) public {
        address newCampaign = address(new FundRaiser(
            clientId,
            propertyId,
            value
        ));
        deploy.push(newCampaign);
    }

    function get() public view returns (address) {
        return deploy[deploy.length - 1];
    }
}

contract FundRaiser {
    string public clientId;
    string public propertyId;
    uint256 public value;

    constructor(
        string memory n,
        string memory i,
        uint256 v
    )  {
        clientId = n;
        propertyId = i;
        value = v;
    }

    function getSummary()
        public
        view
        returns (
            string memory,
            string memory,
            uint256
        )
    {
        return (clientId, propertyId, value);
    }
}
