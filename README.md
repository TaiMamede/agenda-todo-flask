
# agenda-todo-flask

This is a project for Taina learning pourposes

## How to run?

### Installing flask
It's a flask app, so install flask dependency:

> pip install flask


### Running the Mysql database with docker

docker run --name=mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=mysqlroot -d mysql/mysql-server:8.0

### Running the web server (on port 5000)

> flask run
