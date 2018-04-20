"""
Ring Explorer Prototype
This file gets events from the blockchain and stores them in a file
@author: Harnick Khera
"""
import web3
from web3 import Web3, HTTPProvider

w3 = Web3(HTTPProvider("http://localhost:8545")) #connect to local parity node

print(w3.eth.blockNumber) #check connection by looking at the current block number of the partity node

##web3.contract.Contract(address="0x4019440BBe5882915db9F2cAe972a518DB346C62")
#lrcimpl = w3.eth.contract(address="0x4019440BBe5882915db9F2cAe972a518DB346C62")
#lrc = web3.contract.ConciseContract(lrcimpl)
#events = lrc.events

contract_address="0x4019440BBe5882915db9F2cAe972a518DB346C62"
Contract = w3.eth.contract()
contract2 = Contract(address=contract_address)
event_filter = w3.eth.filter({'fromBlock': 0, 'toBlock': 'latest', "address": contract_address})







#print(w3.eth.getBalance('0x0000000000000000000000000000000000010000'))
#fil = w3.eth.getFilterLogs(event_filter.filter_id)
#print(fil)
#print(event_filter.get_all_entries())