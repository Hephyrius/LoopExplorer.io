# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from web3.auto import w3
import web3

print(w3.eth.blockNumber)
contractAddress = "0xb5769656a026e6b910ff976359e9b5d7400b4de4"
implContract = w3.eth.contract(address=contractAddress)
#lrc = web3.eth.Contract('0x55bce3ea76e4f3a5d8c985f6e327058e484a70f9')