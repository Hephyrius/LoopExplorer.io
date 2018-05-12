# LoopExplorer.io

Ring Explorer for the Ethereum implementation of the loopring protocol. 

Written using Bootstrap and Django.

~~[Click here to see a live version](http://LoopExplorer.io:8000)~~ - Offline Until Further Updated/Direction

# Requirements

* Python 3.6
* Django
* MySql
* Pandas

# Tech Stack:

## Front end:
* Bootstrap
* jQuery

## Backend :
* Python
* Django
* MySql

# Ring Data

## Data Sources:
EtherScan.io

## Planned:
* Go Ethereum full node
* Qtum Full node
* Neo Node

# Running

## initializing the Database:

First the MySql database needs to be initialised. 
This should be done by running the ```CreateMysqlDb.sql``` file, 
followed by running ```python manage.py migrate``` from the /ringexplorer directory.
The prototype assumes it is at port 3306, however this will need to be changed to your local MYSQL data base information. 


## populating the database

In order to populate the database run the ImportData.py file In IDLE or via the command:

```
python3 ImportData.py 
```

Currently data importation is a one off process, followed by a constant query service, which queries Etherscan for new Contract Events and fills the database based on values that are not in the DB transactions. For now Etherscan is a viable alternative to a Full Node while the protocol is still being developed extensively.

## starting the server:

In order to run the application run the command in the RingExplore directory

```
python3 manage.py runserver
```
Alternatively Run the ```StartServer.bat``` File in a windows development environment.

This will make the prototype available at : ```http://127.0.0.1:8000/```

## URLs
* http://LoopExplorer.io:8000/ - Homepage
* http://loopexplorer.io:8000/ring/?ringindex=0 - Ring details
* http://LoopExplorer.io:/AllRings/ - Display All Rings in database

# Misc

## planned features short term

* Increasing the diversity of data that is shown ie, addresses of order participants, usd value of orders, token traded, market involved
* Better navigation - footer
* Search functionality to work with miner addresses, ring hash, etc

## LEAF Proposal

see proposals/ directory

# Important

Before deploying on a non-beta production environment, change secret key, admin password and other related security variables.

Author : Harnick Khera












