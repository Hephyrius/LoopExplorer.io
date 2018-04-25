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
    loopringimpl_address = "0xb1170dE31c7f72aB62535862C97F5209E356991b"
    
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
    topic = "0x5b7c7d78703a122ea2c422b2e7bdc79c5da9fc6987bd505b3bef9782c457fd64" 
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
            
            ringsize = len(ContractOutput) - 6
            if ringsize / 2 == 7:
                ringsize = 2
            elif ringsize / 3 == 7:
                ringsize = 3
            else:
                ringsize = 0
            
            orderHashlist = []
            for j in range(ringsize):
                orderHashlist.append(ContractOutput[j+5])
            intList = []
            for j in range((ringsize*6)):
                uint = ContractOutput[j+ringsize+5+1]
                uint = int(uint, 16)/1e18
                intList.append(uint)
            
            ringhash = i['topics'][1]
            miner = "0x"+ContractOutput[1][24:]
            dataSet = {'ringIndex':int(ContractOutput[0], 16), 'ringHash':ringhash, 'miner':miner,'orderHashlist':orderHashlist,'intList':intList}
            block = int(i['blockNumber'], 16)
            timestamp = DT.datetime.fromtimestamp(int(i['timeStamp'],16))
            result=pd.Series([ContractOutput, dataSet, ringsize, i['data'],i['transactionHash'], block, timestamp], index=columns)
            stored_data = stored_data.append(result, ignore_index=True)
            
    #%%
    
    x = conn.cursor()
    
    #insert the data into the db
    for i, row in stored_data.iterrows():
        
        params = ()
        if(row['ringsize'] == 3):
            params = (row['ringsize'], row['dataset']['ringIndex'] , row['block'] , row['timestamp'], "Ethereum", row['dataset']['ringHash'], row['dataset']['miner'], 
                       row['dataset']['orderHashlist'][0], row['dataset']['intList'][0], row['dataset']['intList'][1], row['dataset']['intList'][2] , row['dataset']['intList'][3] , row['dataset']['intList'][4], row['dataset']['intList'][5], 
                       row['dataset']['orderHashlist'][1], row['dataset']['intList'][6], row['dataset']['intList'][7],row['dataset']['intList'][8], row['dataset']['intList'][9], row['dataset']['intList'][10], row['dataset']['intList'][11],
                       row['dataset']['orderHashlist'][2], row['dataset']['intList'][12], row['dataset']['intList'][13], row['dataset']['intList'][14],row['dataset']['intList'][15], row['dataset']['intList'][16],row['dataset']['intList'][17])
        else:
            params = (row['ringsize'], row['dataset']['ringIndex'] , row['block'] , row['timestamp'], "Ethereum", row['dataset']['ringHash'], row['dataset']['miner'], 
                       row['dataset']['orderHashlist'][0], row['dataset']['intList'][0], row['dataset']['intList'][1], row['dataset']['intList'][2] , row['dataset']['intList'][3] , row['dataset']['intList'][4], row['dataset']['intList'][5], 
                       row['dataset']['orderHashlist'][1], row['dataset']['intList'][6], row['dataset']['intList'][7],row['dataset']['intList'][8], row['dataset']['intList'][9], row['dataset']['intList'][10], row['dataset']['intList'][11],
                       0, 0, 0, 0, 0, 0, 0)
        
        cmd = "INSERT INTO web_ring (ringsize, ringindex, block, timestamp, chain, ringhash, mineraddress, order1hash, order1amount, order1nextamount, order1lrcReward, order1lrcFeeState, order1splitS, order1splitB, order2hash, order2amount, order2nextamount, order2lrcReward, order2lrcFeeState, order2splitS, order2splitB, order3hash, order3amount, order3nextamount, order3lrcReward, order3lrcFeeState, order3splitS, order3splitB) VALUES("
        cmd = cmd + "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        x.execute(cmd, (params))
        conn.commit()
    
    #sleep for half a minute before checking again
    time.sleep(60)
#close the connection to the db
x.close()
