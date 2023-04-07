# Full Stack Project 3 - Coffee Shop Full Stack


## Introduction


## Goal
What will I build?

* Display graphics representing the ratios of ingredients in each drink.
* Allow public users to view drink names and graphics.
* Allow the shop baristas to see the recipe information.
* Allow the shop managers to create new drinks and edit existing drinks.


This project will give you a hands-on chance to practice and demonstrate what you've learned in this lesson, such as:

* Implementing authentication and authorization in Flask (Auth0)
* Designing against key security principals
* Implementing role-based control design patterns
* Securing a REST API
* Applying software system risk and compliance principles

The goal is to implement the server by completing the tasks that are listed, which include setting up Auth0, creating a new single-page web application, creating a new API, enabling RBAC, creating new API permissions, creating new roles, testing the endpoints with Postman.
 
 
## Getting Started:

### Tech Stack (Dependencies)

This information is in package.json (Frontend Dependencies) and in requirements.txt (Backend Dependencies)

### 1. Frontend Dependencies

Install Requirements with the following command:
```
npm install
```
#### Development Setup (Frontend)

Running Frontend in Dev Mode
```bash
ionic serve
```

### 2. Backend Dependencies
Our tech stack will include the following:
 * **virtualenv** as a tool to create isolated Python environments
 * **SQLAlchemy ORM** to be our ORM library of choice
 * **PostgreSQL** as our database of choice
 * **Python3** and **Flask** as our server language and server framework
 * **Flask-Migrate** for creating and running schema migrations

Install Requirements with the following command:
```
npm install
```

#### Development Setup (Backend)

1. **Initialize and activate a virtualenv using:**
```
python -m virtualenv env
source env/bin/activate
```
>**Note** - In Windows, the `env` does not have a `bin` directory. Therefore, you'd use the analogous command shown below:
```
source env/Scripts/activate
```

2. **Install the dependencies:**
```
pip install -r requirements.txt
```

3. **Run the development server:**
```
export FLASK_APP=myapp
export FLASK_ENV=development # enables debug mode
python3 app.py
```

4. **Verify on the Browser**<br>
Navigate to project homepage [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

## About the Stack

We started the full stack application for you. It is designed with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask server with a pre-written SQLAlchemy module to simplify your data needs. You will need to complete the required endpoints, configure, and integrate Auth0 for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server. You will only need to update the environment variables found within (./frontend/src/environment/environment.ts) to reflect the Auth0 configuration details set up for the backend app.

[View the README.md within ./frontend for more details.](./frontend/README.md)




## Features
### User
User can do the follwing with authorized permission:

#### Manager

<img src="https://user-images.githubusercontent.com/79179847/230535813-c494fdbb-2a44-44d5-8931-4c91de5062ff.png" alt="Image Description" width="600" >



#### Barista

<img src="https://user-images.githubusercontent.com/79179847/230535876-0c7e2f38-36ea-437f-bc7f-cf476957792c.png" alt="Image Description" width="600" >


### Demo Example

#### backend Postman Test Example (GET drinks-detail)

User can generate JWT token with authorized account login (Auth0) on Frontend web.

<img src="https://user-images.githubusercontent.com/79179847/230534168-aa2761a7-1b81-44ee-bd10-d8ca3f7b4c83.png" alt="Image Description" width="500" >

<img src="https://user-images.githubusercontent.com/79179847/230533746-71b526e0-3399-4f70-88a0-6c08cf5f6a68.png" alt="Image Description" width="500" >


#### Frontend Test Example

Normal User page:

<img src="https://user-images.githubusercontent.com/79179847/230535466-a359b502-17cf-498f-acaf-2cb6979c9034.png" alt="Image Description" width="500" >


Authorized manager page example: can create new drink

<img src="https://user-images.githubusercontent.com/79179847/230535186-7e336c17-3b96-4216-8c48-e889535b41be.png" alt="Image Description" width="500" >


## Tasks Description for this project

The READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)






