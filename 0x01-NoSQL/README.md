# 0x01. NoSQL
`Back-end` `NoSQL` `Python` `MongoDB`

## Learning Outcomes
I learned about the differences between SQL and NoSQL databases, the advantages and disadvantages of NoSQL, and when to use NoSQL vs SQL.
specifically:
- I understood what MongoDB is and how to use it
- I learned how to query MongoDB using `pymongo`
- I understood the concept of `ACID` 
- I learned how to use `MongoDB aggregations`
- I learned how to query or perform `CRUD operations` on a MongoDB database


## Tasks
### [0. List all databases](./0-list_databases.py)
I wrote a Python function that lists all databases in MongoDB.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 0-list_databases.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
simontagbor@ubuntu:~/0x01$
```

### [1. Create a database](./1-use_or_create_database.py)
I wrote a script that creates or uses an existing MongoDB database.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 1-use_or_create_database.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
simontagbor@ubuntu:~/0x01$
```
