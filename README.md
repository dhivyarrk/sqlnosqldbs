Install postgresql service

```
sudo apt install postgresql
```

start postgresql service

```
sudo service postgresql start
sudo service postgresql status
```

connect to postgresql as postgres default user

``` 
sudo -u postgres psql
```

create user with password
```
create user db_user with encrypted password '12345';
```

create a databases
```
create database sql_database;

```

Provide enough privileges for the user to access the database
```
grant all privileges on database asia_database to db_user;
grant create on schema public to db_user;

```

Test if the user has privileges to create table in the database

```
set role db_user;
select currect_user;
CREATE TABLE cars1 (
  name VARCHAR(25),
  model VARCHAR(25),
  year INT
);

drop table cars1;

```
Install from requirement.txt

Create migrations:

```
git clone <repository>
cd multipledb
flask --app=flaskbackendmultipledb db init
flask --app=flaskbackendmultipledb db migrate
flask --app=flaskbackendmultipledb db upgrade
```

Run app

```
flask --app=flaskbackendmultipledb run
```

For information related to postgres database:

Eg:

```
http://127.0.0.1:5000/

choose postgresusersnz and postgres regional products to add, delete, modify products

http://127.0.0.1:5000/sql/usersam
http://127.0.0.1:5000/sql/regionalproducts


Install mongo db :

lucky@lucky-XPS-15-9560:~/Desktop/di/multipledb$ cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=24.04
DISTRIB_CODENAME=noble
DISTRIB_DESCRIPTION="Ubuntu 24.04.1 LTS"

curl -fsSL https://www.mongodb.org/static/pgp/server-8.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list

sudo systemctl start mongod

sudo systemctl daemon-reload

sudo systemctl status mongod



***************************

To get joins of tables from both database

http://127.0.0.1:5000/sqlnosql/combinedregionalproducts