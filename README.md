Django & React Calculator App

Overview

This is a simple calculator application built using Django for the backend and React for the frontend. The app allows users to perform basic arithmetic operations.

Features

Addition, Subtraction, Multiplication, and Division operations

Interactive React-based UI

Django backend for calculations

Tech Stack

Frontend: React, JavaScript, CSS

Backend: Django

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

Node.js (>=14.x)

npm or yarn

Backend Setup (Django)

# Clone the repository
git clone https://github.com/abhisheckpo/django-react-calculator.git
cd Django_Calculator

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py migrate
python manage.py runserver

Frontend Setup (React)

# Navigate to frontend folder
cd calculator_frontend

# Install dependencies
npm install  

# Start React development server
npm start 

Usage

Open the Django server at http://127.0.0.1:8000/

Open the React app at http://localhost:3000/

Use the calculator interface to perform operations.
