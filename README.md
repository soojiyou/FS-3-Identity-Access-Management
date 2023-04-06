# Full Stack Project 3 - Coffee Shop Full Stack


## Introduction


## Goal



## Getting Started:

### Tech Stack (Dependencies)

This information is in package.json (Frontend Dependencies) and in requirements.txt (Backend Dependencies)

### 1. Frontend Dependencies

Install Requirements with the following command:
```
npm install
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

#### Development Setup

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

## Tasks

There are `@TODO` comments throughout the project. We recommend tackling the sections in order. Start by reading the READMEs in:

1. [`./backend/`](./backend/README.md)
2. [`./frontend/`](./frontend/README.md)

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
User can:

1. search Artist, Venue, Show by name.

2. add Artist, Venue, and arrange Show with Artist Id, Venue Id, date.
 
3. edit and delete Artist and Venue information. 

### Demo Example

#### Main Page

<img src="https://user-images.githubusercontent.com/79179847/229996532-5ec1344b-ea3c-4bf0-872d-863a4c123d88.png" alt="Image Description" width="500" >


#### Venue Detail

<img src="https://user-images.githubusercontent.com/79179847/229997167-da05144c-2dd0-45b1-8023-05aace85ccbe.png" alt="Image Description" width="500" >


#### Create new artist

<img src="https://user-images.githubusercontent.com/79179847/229997543-cd2c64e6-e5b6-4184-91d1-cfc4f5e5ae6a.png" alt="Image Description" width="500" >


#### Arrange venue with artist
post show

<img src="https://user-images.githubusercontent.com/79179847/229997786-ed9f3982-0026-4fd4-8fb3-02a5eea68a70.png" alt="Image Description" width="500" >


result show

<img src="https://user-images.githubusercontent.com/79179847/229997913-0a307c40-5cf0-4659-91bb-67897758fac2.png" alt="Image Description" width="500" >




