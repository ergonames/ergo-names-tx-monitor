import requests

ERGO_TESTNET_EXPLORER_API_BASEURL = "https://api-testnet.ergoplatform.com"

def create_url(transactionId):
    url = ERGO_TESTNET_EXPLORER_API_BASEURL + "/api/v1/transactions/" + transactionId
    return url

def get_transaction(transactionId):
    url = create_url(transactionId)
    response = requests.get(url)
    data = response.json()
    return data

def get_transaction_blockid(transaction):
    blockid = transaction['blockId']
    return blockid

def get_transaction_inclusion_height(transaction):
    inclusionHeight = transaction['inclusionHeight']
    return inclusionHeight

def get_transaction_confirmations(transaction):
    confirmations = transaction['numConfirmations']
    return confirmations

def main():

    print("Ergo Names Tx Monitor\n")
    
    txId = "ceca8efce65ea3b54b4904e15bfb907b4a66d5d347d15b4e3b8b5b1a1fa5945d"
    transaction = get_transaction(txId)
    
    blockid = get_transaction_blockid(transaction)
    inclusionHeight = get_transaction_inclusion_height(transaction)
    confirmations = get_transaction_confirmations(transaction)
    
    print(blockid)
    print(inclusionHeight)
    print(confirmations)

if __name__=="__main__":
    main()