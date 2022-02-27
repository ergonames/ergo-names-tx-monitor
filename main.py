import requests
import sys

ERGO_TESTNET_EXPLORER_API_BASEURL = "https://api-testnet.ergoplatform.com"
ERGO_MAINNET_EXPLORER_API_BASEURL = "https://api.ergoplatform.com"

def create_url(transactionId, networkType):
    if networkType == "MAINNET":
        url = ERGO_MAINNET_EXPLORER_API_BASEURL + "/api/v1/transactions/" + transactionId
    elif networkType == "TESTNET":
        url = ERGO_TESTNET_EXPLORER_API_BASEURL + "/api/v1/transactions/" + transactionId
    return url

def get_transaction(transactionId, networkType):
    url = create_url(transactionId, networkType)
    response = requests.get(url)
    data = response.json()
    return data

def get_transaction_blockid(transaction):
    blockid = transaction['blockId']
    return blockid

def main():

    transactionid = str(sys.argv[1])
    networkType = str(sys.argv[2])
    transaction = get_transaction(transactionid, networkType)
    
    blockid = get_transaction_blockid(transaction)

    print(blockid)

if __name__=="__main__":
    main()