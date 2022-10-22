<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a>About The Project</a>
      <ul>
        <li><a>Built With</a></li>
      </ul>
    </li>
    <li>
      <a>Getting Started</a>
      <ul>
        <li><a>Prerequisites</a></li>
        <li><a>Installation</a></li>
      </ul>
    </li>
    <li><a>Usage</a></li>
    <li><a>Roadmap</a></li>
    <li><a>Improvements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This Carbon API will help you know a little more about how much impact the way you travel brings to the planet.

Here's why:
* You will know which is the best transport option for the planet
* You will have the duration and distance of your travel depending the mode of transportation you choice

This project is LIVE on Heroku and can be acceded in this URL:

* https://stark-depths-30347.herokuapp.com/api/transport/

Note: For more information on how to use it go to the Usage part of the file.

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* Python
* Django
* Django Rest-Framework
* Postgres SQL
* Docker
* Heroku
* Gitlab

<!-- GETTING STARTED -->
## Getting Started

There are different ways to run this project, you can:

1. Run the project locally
2. Run the project locally with Docker
3. Run the project directly on Heroku

We will explaining the 3 approaches.

### Prerequisites

Before any configuration, we need to clone the project:

 
  ```sh
  git clone https://github.com/BranddiazTL/carbon-app.git
  ```

### Installation

#####  Run the project locally

With the project clone and on the main directory ./carbon-app, we:
 * Install all libraries
      ```sh
      pip install -r requirements.txt
      ```
 * Make sure we have all the migrations files
      ```sh
      python manage.py makemigrations
      ```
 * Migrate the app
      ```sh
      python manage.py migrate
      ```
 * Run the app
      ```sh
      python manage.py runserver
      ```
   
   
#####  Run the project locally with Docker

First we install [Docker](https://docs.docker.com/get-docker/) if you haven't already done so, after starting Docker in our machine, we:
 * Build the Docker image
      ```sh
       docker build -t web:latest .
      ```
 * Run the container (passing the necessary environment variables)
      ```sh
       docker run -d --name carbon-app -e "PORT=8765" -e "DEBUG=1" -p 8000:8765 web:latest
      ```
 * Make sure the app is running on http://localhost:8000/
 
 * When we finish testing the app, we need to stop the Docker container
      ```sh
       docker stop carbon-app
      ```
   
#####  Run the project with Heroku

First we install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli) if you haven't already done so, and create a [Heroku](https://signup.heroku.com/ ) account, then we:
 * Create a new Heroku app
      ```sh
       heroku create
      ```
 * Add the Django SECRET_KEY to Heroku variables for security (The django secret key is a randomly generated string that's at least 50 characters)
      ```sh
       heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a {YOUR_APP_NAME}
      ```
 
 * Add your app URL to he list of `ALLOWED_HOSTS` on settings.py
      ```sh
       ALLOWED_HOSTS = ['localhost', '127.0.0.1', '{YOUR_APP_NAME}']
      ```
 * Install the heroku-manifest plugin
      ```sh
       heroku update beta
       heroku plugins:install @heroku-cli/plugin-manifest
      ```
 * Add the Heroku app git remote to the project
      ```sh
       heroku git:remote -a {YOUR_APP_NAME}
      ```
 * Push the code to Heroku to build the image and run the Docket container
      ```sh
       git push heroku master
      ```
 * Verify the app is running (it will show a 404 page!)
      ```sh
       heroku open -a {YOUR_APP_NAME}
      ```
 * Finally, verify and run the migrations to Postgres
      ```sh
       heroku run python manage.py makemigrations -a {YOUR_APP_NAME}
       heroku run python manage.py migrate -a {YOUR_APP_NAME}
      ```
 * You can access the Database with
      ```sh
       heroku pg:psql -a {YOUR_APP_NAME}
      ```


<!-- USAGE EXAMPLES -->
## Usage

This project is LIVE on Heroku and can be acceded in this URL:

* https://stark-depths-30347.herokuapp.com/

For more information of the endpoints and parameters visit:

* https://stark-depths-30347.herokuapp.com/api/schema/docs/

To Login to the API we need to use the following endpoint:

* https://stark-depths-30347.herokuapp.com/api/auth/

    * The request body is as follows:
      ```sh
          {
            "username": "user@customer.com",
            "password": "123456789Bb"
          }
      ```
        This is a valid user that can be used to test the app.
        
    * We need to send the token returned on the request in a `Authorization` header in each endpoint request like this:
      ```sh
          Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
      ```

The project has one main API endpoint:

* https://stark-depths-30347.herokuapp.com/api/transport/

    * The endpoint accepts 3 params:
        1. **origin**: `str`, the origin location of the user
            * if you are a registered user you can send origin with the value `home` or `work`
        2. **destination**: `str`, the destination location of the user
            * if you are a registered user you can send destination with the value `home` or `work`
        3. **transport-mode**: `str`, one of `{'driving', 'walking', 'cycling', 'transit', 'all''}`
            * if the transport-mode is send as `all`, all mode of transportation are returned

    * Example:
        * `origin = Dan Ryan Expy, Chicago`
        * `destination = 145 W 46th Pl, Chicago`
        * `transport-mode = all`
        *   URL = https://stark-depths-30347.herokuapp.com/api/transport/?origin=Dan+Ryan+Expy+Chicago&destination=145+W+46th+Pl+Chicago&transport-mode=all
<!-- ROADMAP -->
## Roadmap

- [x] Add Infrastructure, Docker, Heroku and Gitlab CI/CD pipeline
- [x] Add Customer model, serializers and endpoints
- [x] Add Transport app to handle the Distance, Duration and Emissions endpoint
- [x] Add the emissions calculations to the response
- [x] Finish Documentation

<!-- IMPROVEMENTS -->
## Improvements

1. Cache system for most used destinations in general and per user
2. Encryption on personal data like Addresses
3. More accurate Carbon Emissions calculations checking the Make, Model, Car Type and fuel type of the vehicles, comparing the electricity uses of electric cars and the stations where they charge them. Also including different types of Trains, Train Stops and Energy used
4. A good vault integration to handle all the global variables, including settings files for each of the environments 
5. A Custom User model an Authentication, handling refresh tokens, custom internal Authorization tokens for company own services and on
6. A way for the user mark what Transport he decided at the end, to have persistency of the Carbon Emissions history of the user
7. Getting the User City + Region from the location of the device
8. A signal / event implementation to handle the creation of the customer automatically when a user is created
9. ...
  

