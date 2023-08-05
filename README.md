# Catalog_microservices
We have a Catalog Service that handles the company’s “Catalog” (ex: menu of items in a
restaurant); we also have a Service that sends Email notifications to users notifying them that an
item was added to the catalog.

<img width="1088" alt="Screenshot 2023-08-05 at 11 44 08 PM" src="https://github.com/Eslamhathout/Catalog_microservices/assets/21112417/8067ea1f-8963-46a5-8df6-61d9936e3c4f">

# Usage

### Create virtual environments
Open new terminals for each service (catalog / user_notification), activate bothe virtual envrioments, and from each environment, install the serivce requirments using: 

    $ pip install -r requirment.txt

### Create .env files
.env files stores the credetntials/passwords, etc. create a .env file insde each service and populate it using the .env.example keys/values, then override the values with your accounts/passwords.


### Run the two services
From inside each virtual environment, build each service, then start the services

    $ docker-compose build
    $ docker-compose up

Then your services should be running on ports 8000/8001. 

# Postman collection
I've attached the postman collections for both services. [User.postman_collection, Product.postman_collection]
