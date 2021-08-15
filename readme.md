# Article Service


## Steps to run
`
Copy the contents of .env-sample file and create new .env file in local machine
`
```
$ cd nine

$ docker-compose build

$ docker-compose up
```

## API Documentation

```
http://localhost:9000/static/swagger-ui/index.html
```

## System Design

Please read [DESIGN](design/design.md) file.

## E2E Test

- Make sure you have you npm installed in the local machine
```
$ npm -v

$ npm i newman

$ cd nine/main-app/tests

$ newman run MenuPlanningService.postman_collection.json
```

- Alternatively, import MenuPlanningService.postman_collection.json file into your postman app and run the collection.