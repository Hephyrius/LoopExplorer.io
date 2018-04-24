# Ring Explorer

Prototype ring explorer for the loopring protocol. 
Written in Bootstrap and Django.
[Click here to see a live version](https://harnickkhera.com:8000)

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

First the MySql database needs to be initialised. The prototype assumes it is at port 3306. This should be done by running the ```CreateMysqlDb.sql``` file, followed by running ```python manage.py migrate``` from the /ringexplorer directorys

## populating the database

In order to populate the database run the ImportData.py file In IDLE or via the command:

```
python ImportData.py
```

Currently data importation is a one off process, however in a live environment this would be a constant service, which would query blockchain nodes and update the database based on newer transactions. For now Etherscan is a viable alternative while the protocol is still being developed extensively.

## starting the server:

In order to run the application run the command in the RingExplore directory
```
python manage.py runserver 
```

Alternatively Run the ```StartServer.bat``` File in the Django Folder.

This will make the prototype available at : ```http://127.0.0.1:8000/```

## URLs
* http://127.0.0.1:8000/ - Homepage
* http://127.0.0.1:8000/Ring/ - Ring details
* http://127.0.0.1:8000/AllRings/ - Display All Rings in database

# Misc

## notes

Now that the base architecture has been fleshed out, adding new features should be relatively simple.

## planned features short term

* Increasing the diversity of data that is shown ie, addresses of order participants, usd value of orders, token traded, market involved
* Better navigation - Topbar/footer
* Search functionality to work with miner addresses, ring hash, etc

## Issues

* data on the ring page needs to be fixed in order to be shown under the correct categories
* Fix timestamps so they are not 0

## Proposal

see proposals/ directory

# Important

Before deploying on a live environment, change secret key, admin password and other related security variables.

Author : Harnick Khera












