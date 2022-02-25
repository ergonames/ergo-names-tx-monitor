import requests
import sys

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
    
    # Transactions
    # ceca8efce65ea3b54b4904e15bfb907b4a66d5d347d15b4e3b8b5b1a1fa5945d
    # 21f022139807e85fdc75f4a0336dad25843e4675b45981a992149ee32a4f51f9
    # 3be2f15944e39065963ccfe78004b4de2a88228b880d4a08f9bf6e1a0f40f2ab
    # 81689dc62d6c90e7cab2a8bf79dfd51c8e6a892c873e4264611a40dbeb13d953
    #d385642b7400efd636e3f53ea6847677a65952343d611ef31fdcbdef7a3e80d5

    transactionid = str(sys.argv[1])
    transaction = get_transaction(transactionid)
    
    blockid = get_transaction_blockid(transaction)
    inclusionHeight = get_transaction_inclusion_height(transaction)
    confirmations = get_transaction_confirmations(transaction)
    
    print()
    print("Transaction ID\t\t" + str(transactionid))
    print("Block ID\t\t" + str(blockid))
    print("Inclusion Height\t" + str(inclusionHeight))
    print("Confirmation\t\t" + str(confirmations))
    print()

if __name__=="__main__":
    main()