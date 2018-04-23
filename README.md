# Ring Explorer

Prototype ring explorer for the loopring protocol

## Requirements

Python 3.6
Django
Pandas

## Tech Stack:

### Front end:
Bootstrap
jQuery

### Backend :
Python
Django
Sqlite

### Data Sources:
EtherScan.io

#### Planned:
Go Ethereum full node
Qtum Full node
Neo Node

## Running The Prototype:

### Popularing the Database:

In order to populate the database run the ImportData.py folder In IDLE or via the command:

python ImportData.py

Currently data importation is a one off process, however in a live environment this would be a constant service, which would query blockchain nodes and update the database based on newer transactions. For now Etherscan is a viable alternative while the protocol is still being developed extensively.

### Running the server:
In order to run the application run the command in the Django/RingExplore directory

python manage.py runserver Alternatively Run the StartServer.bat File in the Django Folder.

This will make the prototype available at : http://127.0.0.1:8000/

