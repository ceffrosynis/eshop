# crypto-wallet
## Cryptocurrency Wallet

Crypto Wallet gives you the opportunity to create cryptocurrency wallets by just creating your personal account and generating a new public key for the currency you are interested in.

## Technical Overview
This is a full-stack web application which is written in Python by making use of the Django Web Framework.

## Directory Structure

    .
    ├── ...
    ├── docs                    # Documentation files (alternatively `doc`)
    │   ├── TOC.md              # Table of contents
    │   ├── faq.md              # Frequently asked questions
    │   ├── misc.md             # Miscellaneous information
    │   ├── usage.md            # Getting started guide
    │   └── ...                 # etc.
    └── ...


## Installation

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Database Initialization & Update

You have to create the tables in the database before you can use them
```
python manage.py migrate
```
In order to apply some changes (Update) to your model you have to run
```
python manage.py makemigrations
```
## Start the Server

```
python manage.py runserver
```
## App Presentation

###### **Login Page**
![alt text](https://github.com/ceffrosynis/crypto-wallet/blob/main/pics/Login%20Page.png)

###### **Registration Page**
![alt text](https://github.com/ceffrosynis/crypto-wallet/blob/main/pics/Registration%20Page.png)

###### **Edit Profile Page**
![alt text](https://github.com/ceffrosynis/crypto-wallet/blob/main/pics/Edit%20Profile%20Page.png)

###### **My Wallet Page**
![alt text](https://github.com/ceffrosynis/crypto-wallet/blob/main/pics/My%20Wallet%20Page.png)

###### **Search Results Page**
![alt text](https://github.com/ceffrosynis/crypto-wallet/blob/main/pics/Search%20Results%20Page.png)
