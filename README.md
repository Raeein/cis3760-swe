# CIS*3760 Project Template

This project will serve as a guide on how to setup a three part application that includes a Spring server, a SQL database and a React frontend both locally and on a Kubernetes host.

## Local Setup

To setup the project locally, you must have [docker](https://www.docker.com/products/docker-desktop/) installed and running on your machine. Once it is setup, run the following command:

```
docker compose up
```

This will setup the app and you can access the following addresses on your browser:
- React frontend = http://localhost:3000
- Spring backend = http://localhost:8080/api (add **/docs.html** to access Swagger UI)

## Testing
To run the tests for the Java and Python applications, run the following command:

```
make test
```

If the user does not have make installed on their computer, please run this instead:

```
docker-compose -f test.yml up --build
```

## Development Tips
- Run `docker compose up --build` to rebuild the containers
- When developing the MariaDB database remove the volumes to reset the database or your changes will not be reflected `docker compose down -v`
