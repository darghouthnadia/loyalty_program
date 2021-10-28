# loyalty_program

## Description
This is an implementation of the microservice for discount code. It's build using django rest framework and Docker. I'm using the default DB of django : SQLITE3.
Due to lack of time there's no frontend. 

## How to install the app locally
Since it's docker, it's fairly easy :
* Make sure you have docker installed on your machine
* Clone the repo
* Position yourself on the directory where the Docker files are
* Open the terminal
* Run `docker-compose pull`
* Run `docker-compose up -d --build`
* The api will run on `http://localhost:8000`

## API urls available:
*  `http://localhost:8000/discountcode/` : 
  * GET: List all discount codes
  * POST: Generate X codes for a specified brand
* `http://localhost:8000/brand/`:
  * POST: Create a brand
  * GET: List of all brands
* `http://localhost:8000/follower/`:
  * POST: Create a follower (retrieve a code and create a follower which is basically the relation between a brand and the user)
  * GET: List of all followers (this is not working as the time of writing this)

## Miscellaneous:
* Both producer.py and consumer.py are 'skeletons', they are connected to my personal cloudRabbitMQ but mostly as to show the code and discuss it.
* The documentation for the endpoints are missings, if i had more time i would have created it using Swagger. 


