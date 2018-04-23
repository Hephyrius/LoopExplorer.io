# Ring Explorer

Prototype ring explorer for the loopring protocol

# Requirements

Python 3.6
Django
Pandas

# Tech Stack:

## Front end:
Bootstrap
jQuery

## Backend :
Python
Django
MySql

# Ring Data

## Data Sources:
EtherScan.io

## Planned:
Go Ethereum full node
Qtum Full node
Neo Node

# Running

## initializing the Database:

First the MySql database needs to be initialised. The prototype assumes it is at port 3306. This should be done by running the "CreateMysqlDb.sql" file, followed by running "python manage.py migrate" in the /ringexplorer directorys

## populating the database

In order to populate the database run the ImportData.py file In IDLE or via the command:

python ImportData.py

Currently data importation is a one off process, however in a live environment this would be a constant service, which would query blockchain nodes and update the database based on newer transactions. For now Etherscan is a viable alternative while the protocol is still being developed extensively.

## starting the server:

In order to run the application run the command in the Django/RingExplore directory

python manage.py runserver Alternatively Run the StartServer.bat File in the Django Folder.

This will make the prototype available at : http://127.0.0.1:8000/

## URLs
http://127.0.0.1:8000/ - Homepage
http://127.0.0.1:8000/Ring/ - Ring details
http://127.0.0.1:8000/AllRings/ - Display All Rings in database

