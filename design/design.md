# Tech Stack

- Python 3
- Flask as web framework
- PeeWee as ORM
- Docker as Container
- SQLite as a database
- Postman for E2E test
- Swagger UI for API Documentation

# Why this tech stack?

- I choose python as my primary development language instead of Go (preferred) because I'm still an intermediate level in Go and dont know much about the best practices and frameworks used to structure the codebase. Also, without using a standardarized development method in Go, it would have gone against me. Hence, python! (I'm interested to learn Go though).

- I choose peewee as the ORM as it is a simple and small ORM. It has few (but expressive) concepts, making it easy to learn and intuitive to use.

- I choose this service to be dockerized, as it eliminates the gold old saying `it works on my system`.

- I choose SQLite as the db is its easy and lightweighted relational database.

- I choose Postman to do my E2E tests as it is standarized and doesnt require much installation setup or external libraries.

- I choose to have all the APIs documented in Swagger as it gives much more insights for the APIs instead of relying on inline comments. Through this one can easily run and test the apis without having to install anything 3rd party software or module.

# System Achitecture

![System Architecture Diagram](system_arch.png?raw=true "System Architecture")
## Presentation Layer
- The scope of the project was not to implement the frontend.
- Instead of creating a frontend, Swagger UI documentation for REST API is created.
- This allows to communicate with the application layer via HTTP requests and responses.
- This provides a quick API working check and is a well documented UI which gives information about the API.

## Application Layer
- This layer contains all the bussiness logic of the application.
- The article microservice is containerzied using Docker.
- This microservice can now be used as a plug-n-play service for any existing product.
- The enpoints are developed using Python and Flask.
- - /auth - POST apis for login and signup, gives JWT token in return. This token is sent in subsiquent requests for user authentication.
- - /article - POST api to create a new articles and its tags. GET api to fetch the recipe by articleId in path params.
- - /tags - GET api returns lists of articles that have that tag name on the given date and some summary data about that tag for that day.
- All the corresponding functions are written using python and its libraries.
- These functions create corresponding entity classes whihc are later mapped to the database in the data layer.

## Data Layer
- This layer is developed using SQLite relational databse.
- Objects gets passed to the Object Relation Mapping (ORM) from the application layer.
- This ORM is developed using python peewee.
- Peewee maps the entity to the SQLite database and using CRUD operations does the talking with the db.


# ER Diagram

![ER Diagram](ER.png?raw=true "ER Diagram")

## Explaination of the above diagram

- Users table has columns such as `id as primary key`, uuid, username and password.
- Users can have many articles published. Hence there is a `1:N relation` between Users and Articles table.
- Articles table has columns such as `id as primary key`, uuid, `user_id as a foreign key` from Users table, title, body and date.
- TagNames table has columns `id as primary key` and name, which is unique.
- Many Articles can have many TagNames. Hence there is a `M:N relation` between Articles and TagNames Table.
- Whenever there is M:N relation, another table is created and here another table Tags is created with columns `id as primary key`, `article_id as foreign key` from Articles table and `tag_id as foreign key` from TagNames table.


# About the test

- I think this is one the best way to judge a software developer by giving them these kinds of problems instead tricky algorithmic questions. Those questions can really be found anywhere on the internet and will never give the actual insights about a person on thier codebase management skills.
- It really tests everything from the codebase knowledge to in depth database knowledge and connecting them to the endpoints and having the business logic in between.
- I thoroghly enjoyed developing the solution and I'm sure you'll be able to judge me better through this submission. Thanks!

# Improvements

- If I had time i would have added a frontend service to it (basic) developed in reactJS.
- I would have deployed this microservice to any cloud platform such as AWS for better accessibility, availability and scalability.
- I would have opted for a much mature relational database such as PostgreSQL instead of SQLite.
- I would have also implemented this solution in Go instead of Python.