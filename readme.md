
# E Trade System RestAPI (Django)

API project developed with django rest framework covering all the features of an e-commerce system


## Features

- User Authentication System ( Login,Register etc. with JWT)
- Throttle System for Cyber Security (Bruteforce Attacks etc.)
- Seller and Customer System
- Cart System
- Order System (With Payment (Credit Card))
- Product System
- Favorite Product System
- Product Comment System
    
## Tech Stack

**Server:** Django, Rest Framework

## Run Locally

Clone the project

```bash
  git clone https://github.com/Brktrlw/E-trade-With-RestAPI
```

Go to the project directory

```bash
  cd E-trade-With-RestAPI/core
```
Create Virtual Env
```bash
  python -m venv env
```
```bash
  .\env\Scripts\activate
```


Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python3 manage.py runserver
```


## API

#### Cart System

```http
http://127.0.0.1/api/carts/
```

| API | Description | Parameters | Auth|
|:-------- |  :------ |:------------------------------------------- |:--
|` POST /addtocart/<productSlug>` | Add product to cart   | amount| X
|` DEL /reducetocart/<productSlug>` | Reduce product's amount from cart |amount |X
|` DEL /deletetoproduct/<productSlug>` | Delete product from cart | |X
|` PUT /updatecart/<productSlug>` | Update product's amount from cart |amount |X
|` GET /list/` | List user's cart items | |X

#### Comment System

```http
http://127.0.0.1/api/comments/
```

| API | Description | Parameters | Auth|
|:-------- |  :------ |:------------------------------------------- |:--
|` GET /list/<productSlug>` | List comments' by product   | | |
|` POST /create/<productSlug>` | Add comment to product |comment |X
|` DEL /delete/<unique_id>` | Delete comment from product | |X
|` UPDATE /update/<unique_id>` | Update comment  |comment |X


#### Order System

```http
http://127.0.0.1/api/orders/
```

| API | Description | Parameters | Auth|
|:-------- |  :------ |:------------------------------------------- |:--
|` POST /create/` | Create order | addressId,payment| X|
|` GET /list/` | List user's orders | |X
|` GET /detail/<unique_id>` | List order detail | | X|

#### User System

```http
http://127.0.0.1/api/user/
```

| API | Description | Parameters | Auth|
|:-------- |  :------ |:------------------------------------------- |:--
|` POST /register/` | User Register | username,password,password2,email,first_name,last_name,isCustomer| |
|` POST /token/` | User Login |username,password ||
|` POST /refresh/` | Refresh Token | refresh ||
|` DEL /delete/` | User Delete |  || X

## Feedback

If you have any feedback, please reach out to us at berkaygithub@protonmail.ch

## Developers

- [@brktrllz](https://www.instagram.com/brktrll.z)
