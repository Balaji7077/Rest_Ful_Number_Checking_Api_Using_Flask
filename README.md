# Python Number Programs API

This repository contains a collection of Python number-related programs, implemented as Flask APIs. The goal is to check whether a given number satisfies certain properties, such as being an Armstrong Number, Disarium Number, Spy Number, Emirp Number, and so on.

Each program is exposed as a separate API endpoint using Flask.

# List of Programs

1.Armstrong Number

2.Disarium Number

3.Spy Number

4.Emirp Number

#1. Armstrong Number

An Armstrong Number (or Narcissistic Number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.

# Endpoint: /armstrong/<int:num>

GET request to check if a number is an Armstrong number.

# Example:

GET http://127.0.0.1:5000/armstrong/153

# Response:

For Armstrong Number (e.g., 153):


{

    "number": 153,
    "is_armstrong_number": true
}


# 2. Disarium Number

A Disarium Number is a number where the sum of its digits raised to the power of their respective positions equals the number itself.

# Endpoint: /disarium/<int:num>

GET request to check if a number is a Disarium number.

# Example:

GET http://127.0.0.1:5000/disarium/135

# Response:

For Disarium Number (e.g., 135):

{

    "number": 135,
    "is_disarium_number": true
}


# 3. Spy Number

A Spy Number is a number where the sum of its digits equals the product of its digits.

# Endpoint: /spy/<int:num>

GET request to check if a number is a Spy number.

# Example:

GET http://127.0.0.1:5000/spy/123
# Response:

For Spy Number (e.g., 123):


{

    "number": 123,
    "is_spy_number": true
}

# 4. Emirp Number

An Emirp Number is a prime number whose reverse is also a prime number, but the number and its reverse are not the same.

# Endpoint: /emirp/<int:num>

GET request to check if a number is an Emirp number.

# Example:

GET http://127.0.0.1:5000/emirp/17
# Response:

For Emirp Number (e.g., 17):


{

    "number": 17,
    "is_emirp_number": true
}

# How to Run the Project

### 1.Clone the repository:

git clone https://github.com/Balaji7077/Rest_Ful_Number_Checking_Api_Using_Flask.git

### 2.Navigate to the project directory:

cd Rest_Ful_Number_Checking_Api_Using_Flask

### 3.Install the required dependencies:

pip install flask

### 4.Run the Flask application:

python main.py

### 5.Access the API at:

http://127.0.0.1:5000
