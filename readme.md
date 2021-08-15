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

## System Design

Please read [DESIGN](design/design.md) file.

## API Documentation

```
http://localhost:9000/static/swagger-ui/index.html
```


## E2E Test

- Make sure you have you npm installed in the local machine
```
$ npm -v

$ npm i newman

$ cd nine/main-app/tests

$ newman run nine.postman_collection.json
```

- Alternatively, import nine.postman_collection.json file into your postman app and run the collection.