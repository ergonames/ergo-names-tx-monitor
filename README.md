# Ergo Names Tx Monitor

Will return a box ID for a given transaction. Needs a transaction ID in order to run.

### Use

To run enter

```
python3 main.py {transactionId} {networkType}
```

where {transactionId} is a the ID of a transaction on the Ergo blockchain and {networkType} is either MAINNET or TESTNET.

### Example

Command to start the program:

```shell Mainnet
python3 main.py 0c112378382b8b53f5f3463bbb56f0639e9bbe8244ea953cce7214a700532f97 MAINNET
```
```shell Testnet
python3 main.py ceca8efce65ea3b54b4904e15bfb907b4a66d5d347d15b4e3b8b5b1a1fa5945d TESTNET
```

Output:

```shell Mainnet
a67d23316cc806af535e43ef73ceb0c7e78a175322f36e01a033323174829978
```
```shell Testnet
2d696e57c99615d88379cfb9a66e673f47d95589be6e74020006d3a937a41dc1
```