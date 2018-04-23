# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:05:30 2018

@author: Khera
"""
#library imports
import numpy as np
import pandas as pd
import requests
import json
import sqlite3 
import os
import datetime as DT

#api ley for etherscan
api_key = "3YT45XBZMKGYDF8IDECEXN8V4M9FX59MH7"

#loopringimpl deployment address
loopringimpl_address = "0x4019440BBe5882915db9F2cAe972a518DB346C62"

#api endpoint and parameters for requesting of data
endpoint = "https://api.etherscan.io/api?module=logs&action=getLogs"
from_block = "0"
to_block = "latest"

#constructing the api reqruest
request = endpoint + "&fromBlock=" + from_block + "&toBlock=" + to_block + "&address=" + loopringimpl_address + "&apikey="+api_key

#getting the data from the server
data = requests.get(request).json()['result']

#process data and find instances where the topic is the ring mined topic
columns = ["data","dataset","ringsize","rawdata", "transactionhash", 'block', 'timestamp']
stored_data = pd.DataFrame(columns=columns)
topic = "0x36fe6e0e52b9db0206978557b0c50ef564aeb27c4fce2455a2f459aeefefc23b" 
data2 = []
for i in data:
    if topic in i['topics']:
        data2.append(i)

#iterate over the data and extract the relevant parts, processing accordingly
for i in data2:
    ContractOutput = []
    for j in range(2,len(i['data']),64):
        ContractOutput.append(i['data'][j:j+64])
        
    ringsize = len(ContractOutput) - 7
    if ringsize % 2 == 0:
        ringsize = 2
    elif ringsize % 3 == 0:
        ringsize = 3
    else:
        ringsize = 0
    
    orderHashlist = []
    for j in range(ringsize):
        orderHashlist.append(ContractOutput[j+6])
    intList = []
    for j in range((ringsize*6)):
        uint = ContractOutput[j+ringsize+6+1]
        uint = int(uint, 16)
        intList.append(uint)
    
    ringhash = ContractOutput[1][24:]
    miner = "0x"+ContractOutput[3][24:]
    feerecp = "0x"+ContractOutput[4][24:]
    dataSet = {'ringIndex':int(ContractOutput[0], 16), 'ringHash':ringhash, 'miner':miner,'feeRecipient':feerecp,'orderHashlist':orderHashlist,'intList':intList}
    block = int(i['blockNumber'], 16)
    timestamp = 0 # TODO
    result=pd.Series([ContractOutput, dataSet, ringsize, i['data'],i['transactionHash'], block, timestamp], index=columns)
    stored_data = stored_data.append(result, ignore_index=True)
    
#%%
    
##create a sqlite file
#conn = sqlite3.connect(r"Data.db")
#c = conn.cursor()
#c.execute("""CREATE TABLE ringdata
#                 (ringsize, ringindex, block, timestamp, chain, ringhash, mineraddress, minerlrc, minerx, minery, minerz, address01, traded01, market01, amount01, fill01, lrcfee01, orderhash01, feepaid01, address02, traded02, market02, amount02, fill02, lrcfee02, orderhash02, feepaid02, address03, traded03, market03, amount03, fill03, lrcfee03, orderhash03, feepaid03)""")
#%%
#insert the data into the db
for i, row in stored_data.iterrows():
    command = "INSERT INTO ringdata (ringsize, ringindex, block, timestamp, chain, ringhash, mineraddress, minerlrc, minerx, minery, minerz, address01, traded01, market01, amount01, fill01, lrcfee01, orderhash01, feepaid01, address02, traded02, market02, amount02, fill02, lrcfee02, orderhash02, feepaid02, address03, traded03, market03, amount03, fill03, lrcfee03, orderhash03, feepaid03)"
    command = command + " \nvalues(" + str(row['ringsize']) +", " + str(row['dataset']['ringIndex']) +", "+ str(row['block']) +", "+ str(row['timestamp']) +", Ethereum, " + str(row['dataset']['ringHash']) +", " + str(row['dataset']['miner']) +", "
    print(command)
    #c.execute(command)
#conn.close()

#%%








































#topic = "0x36fe6e0e52b9db0206978557b0c50ef564aeb27c4fce2455a2f459aeefefc23b"
#topic1 = "0x80af788bd76e7a6ea808e34ec8ad3feb8f1d044df699e01824c9a64ca7c2742c"
#topicRequest = request = endpoint + "&fromBlock=" + from_block + "&toBlock=" + to_block + "&address=" + loopringimpl_address + "&topic=" + topic1 + "&apikey="+api_key
#
#topicData = requests.get(topicRequest).json()['result']