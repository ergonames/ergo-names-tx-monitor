import json
import urllib3
import boto3

ERGO_MAINNET_EXPLORER_API_BASEURL = "https://api.ergoplatform.com"
ERGO_TESTNET_EXPLORER_API_BASEURL = "https://api-testnet.ergoplatform.com"

SQS_QUEUE_URL = ""

def create_url(transactionId, networkType):
    restOfUrl = "/api/v1/transactions/" + transactionId
    if networkType == "MAINNET":
        url = ERGO_MAINNET_EXPLORER_API_BASEURL + restOfUrl
    elif networkType == "TESTNET":
        url = ERGO_TESTNET_EXPLORER_API_BASEURL + restOfUrl
    return url

def get_transaction_data(transactionId, networkType):
    http = urllib3.PoolManager()
    url = create_url(transactionId, networkType)
    response = http.request('GET', url)
    transactionData = response.data
    return transactionData

def get_transaction_blockid(transactionData):
    jsonData = convert_http_response_to_json(transactionData)
    blockid = jsonData['blockId']
    return blockid
    
def convert_http_response_to_json(responseData):
    jsonData = json.loads(responseData)
    return jsonData

def lambda_handler(event, context):
    transactionId = event.get("transactionId")
    networkType = event.get("networkType")
    transaction = get_transaction_data(transactionId, networkType)
    blockId = get_transaction_blockid(transaction)
    
    sqs = boto3.client('sqs')
    response = sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        DelaySeconds=0,
        MessageAttributes={
            'transactionId': {
                'DataType': 'String',
                'StringValue': transactionId
            },
            'networkType': {
                'DataType': 'String',
                'StringValue': networkType
            },
            'blockId': {
                'DataType': 'String',
                'StringValue': blockId
            }
        },
        MessageBody=(
            "Transaction Information with BlockId"
        )
    )
    return {
        'statusCode': 200,
        'body': blockId
    }
