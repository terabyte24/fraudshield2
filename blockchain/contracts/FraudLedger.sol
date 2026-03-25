// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract FraudLedger {
    struct FraudRecord {
        string ringId;
        bytes32 dataHash;
        uint8 riskScore;
        uint256 timestamp;
        address submitter;
    }

    FraudRecord[] public records;
    mapping(string => bool) public exists;

    event FraudSubmitted(string ringId, bytes32 dataHash, uint8 riskScore);

    function submitFraud(string memory ringId, bytes32 dataHash, uint8 riskScore) public {
        require(!exists[ringId], "Ring ID already exists");
        records.push(FraudRecord({
            ringId: ringId,
            dataHash: dataHash,
            riskScore: riskScore,
            timestamp: block.timestamp,
            submitter: msg.sender
        }));
        exists[ringId] = true;
        emit FraudSubmitted(ringId, dataHash, riskScore);
    }

    function getRecord(uint256 index) public view returns (FraudRecord memory) {
        return records[index];
    }

    function totalRecords() public view returns (uint256) {
        return records.length;
    }
}
