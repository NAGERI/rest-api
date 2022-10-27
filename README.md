# Backend setup

This is a simple application that returns a resoponse based on the `GET` HTTP requests.

## GET

GET is used to request data from a specified resource.

- GET requests can be cached
- GET requests remain in the browser history
- GET requests can be bookmarked
- GET requests should never be used when dealing with sensitive data
- GET requests have length restrictions
- GET requests are only used to request data (not modify)

source: w3Schools

## Usage

- clone this repository

`git clone https://github.com/NAGERI/rest-api.git .`

Make sure you have python installed.

- Install the virtual env

`pip install virtualenv`

- Create a virtual environment

`python -m virtualenv env`

- Activate the virtual environment

`source env/Scripts/activate`

- Install the required dependancies

`pip install -r requirements.txt`

- Run the application, on your local machine

`python manage.py runserver`
