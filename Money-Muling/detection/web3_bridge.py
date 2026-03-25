import json
import hashlib
from web3 import Web3
import os

def get_contract_info():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    info_path = os.path.join(base_dir, "contract_info.json")
    if not os.path.exists(info_path):
        return None
    with open(info_path, "r") as f:
        return json.load(f)

def get_web3():
    return Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

def submit_fraud_ring(ring_id, risk_score, members):
    w3 = get_web3()
    contract_info = get_contract_info()
    if not contract_info:
        raise Exception("Contract info not found. Has it been deployed?")
    
    contract = w3.eth.contract(address=contract_info["address"], abi=contract_info["abi"])
    
    sorted_members = sorted(members)
    members_json_bytes = json.dumps(sorted_members, separators=(',', ':')).encode('utf-8')
    data_hash = hashlib.sha256(members_json_bytes).digest()
    
    account_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
    account = w3.eth.account.from_key(account_key)
    sender_address = account.address
    
    tx = contract.functions.submitFraud(
        ring_id,
        data_hash,
        int(risk_score)
    ).build_transaction({
        'from': sender_address,
        'nonce': w3.eth.get_transaction_count(sender_address),
        'gas': 200000,
        'gasPrice': w3.to_wei('1', 'gwei')
    })
    
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=account_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    return {
        "tx_hash": receipt.transactionHash.hex(),
        "block_number": receipt.blockNumber,
        "status": receipt.status
    }

def get_all_records():
    w3 = get_web3()
    contract_info = get_contract_info()
    if not contract_info:
        return []
    
    contract = w3.eth.contract(address=contract_info["address"], abi=contract_info["abi"])
    
    total = contract.functions.totalRecords().call()
    records = []
    
    for i in range(total):
        record = contract.functions.getRecord(i).call()
        data_hash_val = record[1]
        data_hash_hex = data_hash_val.hex() if isinstance(data_hash_val, bytes) else data_hash_val
        records.append({
            "ringId": record[0],
            "dataHash": data_hash_hex,
            "riskScore": record[2],
            "timestamp": record[3],
            "submitter": record[4]
        })
        
    return records
