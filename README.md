# e-Book
## Online Bookstore


e-Book is a simple full-stack e-commerce web application, which is written in Python, by using the Django Web Framework. Each user, in order to be able to use the platform, has to create a profile by providing some necessary information.

Each user can:

* Insert a new product (sell) by giving:
    * Quantity
    * Price
    * Description  
* Buy a product

## Project Objective
The objective in this project is to become familiar with the **main logic of an e-commerce app** and **the Django Web Framework**

## Directory Structure

    .
    ├── ebook
    │   ├── ebook             # Project's main directory
    │   ├── eshop             # Application's main logic
    │   │   ├── ...
    │   │   ├── static        # Application's static files
    │   │   ├── templates     # Application's templates (Home Page, Cart Page, Login Page ...)
    │   │   ├── templatetags  # A template tag for computing the total quantity
    │   │   └── ...
    │   ├── media             # App's images
    │   └── ...
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
![alt text](https://github.com/ceffrosynis/eshop/blob/main/pics/Log%20In%20Page.png)

###### **Registration Page**
![alt text](https://github.com/ceffrosynis/eshop/blob/main/pics/Register%20Page.png)

###### **Edit Info Page**
![alt text](https://github.com/ceffrosynis/eshop/blob/main/pics/Edit%20Info%20Page.png)

###### **My Cart Page**
![alt text](https://github.com/ceffrosynis/eshop/blob/main/pics/Cart%20Page.png)

###### **Checkout Page**
![alt text](https://github.com/ceffrosynis/eshop/blob/main/pics/Checkout%20Page.png)
