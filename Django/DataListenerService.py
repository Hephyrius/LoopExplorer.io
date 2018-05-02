# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:47:12 2018

@author: Khera
"""

"""
Code responsible for extracting data from etherscan
@author: Harnick Khera
"""
#library imports
import numpy as np
import pandas as pd
import requests
import json
import os
import datetime as DT
import MySQLdb
import time
#%%

#connect to mysql
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  db="ring")
while(True):
    #get the "best"/Highest index from the db
    x = conn.cursor()
    x.execute('SELECT max(ID) FROM web_ring')
    maxInd = x.fetchall()[0][0]
    
    
    #api ley for etherscan
    api_key = "3YT45XBZMKGYDF8IDECEXN8V4M9FX59MH7"
    
    #loopringimpl deployment address
    loopringimpl_address = "0x8d8812b72d1e4ffCeC158D25f56748b7d67c1e78"
    
    version = "1.5.1"
    
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
    topic = "0x4d2a4adf7c5f6cf35d97aecc1919897bf86299dccd9b5e19b2b38ebebf07add0" 
    
    data2 = []
    for i in data:
        if topic in i['topics']:
            data2.append(i)
    
    #iterate over the data and extract the relevant parts, processing accordingly
    #process only happens when the index is greater than the expected index
    for i in data2:
    
        ContractOutput = []
        for j in range(2,len(i['data']),64):
            ContractOutput.append(i['data'][j:j+64])
            
        ringIdx = int(ContractOutput[0], 16)
        if ringIdx >= maxInd:
            
            ringsize = len(ContractOutput) - 5
            if ringsize / 2 == 7:
                ringsize = 2
            elif ringsize / 3 == 7:
                ringsize = 3
            else:
                ringsize = 0
            
            #lists to store treated data
            orderHashlist = []
            owners = []
            tokens = []
            intList = []  
            
            #iterate over orderingolist and convert data depending on type
            for j in range(0,(ringsize*7)):
                if j == 0 or j==7 or j==14:
                    orderHashlist.append(ContractOutput[j+5])
                elif j == 1 or j==8 or j==15:
                    owner = "0x"+ContractOutput[j+5][24:]
                    owners.append(owner)
                elif j == 2 or j==9 or j==16:
                    token = "0x"+ContractOutput[j+5][24:]
                    tokens.append(token)
                else:
                    uint = ContractOutput[j+5]
            
                    uint = int(uint, 16)/1e18
                    intList.append(uint)
        
            #treat misc items
            ringhash = i['topics'][1]
            miner = "0x"+ContractOutput[1][24:]
            block = int(i['blockNumber'], 16)
            timestamp = DT.datetime.fromtimestamp(int(i['timeStamp'],16))
            
            #store values in preparation for data being imported into db
            dataSet = {'ringIndex':int(ContractOutput[0], 16), 'ringHash':ringhash, 'miner':miner,'orderHashlist':orderHashlist,'intList':intList, 'owners':owners, 'tokens':tokens}
            result=pd.Series([ContractOutput, dataSet, ringsize, i['data'],i['transactionHash'], block, timestamp], index=columns)
            stored_data = stored_data.append(result, ignore_index=True)
            
    #%%
    
    x = conn.cursor()
    
    #insert the data into the db
    for i, row in stored_data.iterrows():
        
        params = ()
        if(row['ringsize'] == 3):
            params = (row['ringsize'], row['dataset']['ringIndex'] , row['block'] , row['timestamp'], "Ethereum", version, row['dataset']['ringHash'], row['dataset']['miner'], 
                       row['dataset']['orderHashlist'][0], row['dataset']['owners'][0], row['dataset']['tokens'][0], row['dataset']['intList'][0], row['dataset']['intList'][1], row['dataset']['intList'][2] , row['dataset']['intList'][3], 
                       row['dataset']['orderHashlist'][1], row['dataset']['owners'][1], row['dataset']['tokens'][1], row['dataset']['intList'][4], row['dataset']['intList'][5], row['dataset']['intList'][6] , row['dataset']['intList'][7], 
                       row['dataset']['orderHashlist'][2], row['dataset']['owners'][2], row['dataset']['tokens'][2], row['dataset']['intList'][8], row['dataset']['intList'][9], row['dataset']['intList'][10] , row['dataset']['intList'][11])
        else:
            params = (row['ringsize'], row['dataset']['ringIndex'] , row['block'] , row['timestamp'], "Ethereum", version, row['dataset']['ringHash'], row['dataset']['miner'], 
                       row['dataset']['orderHashlist'][0], row['dataset']['owners'][0], row['dataset']['tokens'][0], row['dataset']['intList'][0], row['dataset']['intList'][1], row['dataset']['intList'][2] , row['dataset']['intList'][3], 
                       row['dataset']['orderHashlist'][1], row['dataset']['owners'][1], row['dataset']['tokens'][1], row['dataset']['intList'][4], row['dataset']['intList'][5], row['dataset']['intList'][6] , row['dataset']['intList'][7], 
                       0, 0, 0, 0, 0, 0, 0)
        
        cmd = "INSERT INTO web_ring (ringsize, ringindex, block, timestamp, chain, version, ringhash, mineraddress, order1hash, order1owner, order1token, order1fillamount, order1lrcReward, order1lrcFeeState, order1splitS, order2hash, order2owner, order2token, order2fillamount, order2lrcReward, order2lrcFeeState, order2splitS, order3hash, order3owner, order3token, order3fillamount, order3lrcReward, order3lrcFeeState, order3splitS) VALUES("
        cmd = cmd + "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        x.execute(cmd, (params))
        conn.commit()
    
    #sleep for half a minute before checking again
    time.sleep(60)
#close the connection to the db
x.close()
