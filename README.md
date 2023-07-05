# Blog Mangement System

## Introduction
This is a basic Django web application with REST APIs for a fictional Blog Post Management System, with minimal frontend. The app supports two types of user roles: Admin and User. The APIs have been designed using Django Rest Framework and tested using Postman.

## Installation
1. Clone the repository to your local machine using the following command:

`https://github.com/yuvraj279/Blog-Mangement-System.git`

2. Navigate to the project directory:

`cd your-project-directory`

3. Create a virtual environment:

`python -m venv venv`

4. Activate the virtual environment:

    For Windows:

    `venv\Scripts\activate`

    For Linux/Mac:

    `source venv/bin/activate`

5. Install the project dependencies:

`pip install -r requirements.txt`

6. Set up the database:

`python manage.py migrate`


## Running the Application

To run the application, execute the following command in your terminal or command prompt:

`python manage.py runserver`

Once the server is running, you can access the application in your web browser at http://localhost:8000/.
