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

### [2. Insert document](./2-insert.py)
I wrote a script that inserts a document in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 2-insert.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
simontagbor@ubuntu:~/0x01$
```
### [3. All documents](./3-all.py)
I wrote a script that lists all documents in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 3-all.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5f1d7a5d9c6a6a2b4b1c371e"), "name" : "Bob" }
{ "_id" : ObjectId("5f1d7a5d9c6a6a2b4b1c371f"), "name" : "John" }
{ "_id" : ObjectId("5f1d7a5d9c6a6a2b4b1c3720"), "name" : "Betty" }
```
### [4. All matches](./4-match.py)
I wrote a script that lists all documents with `name="Holberton School"` in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 4-match.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
simontagbor@ubuntu:~/0x01$
```
### [5. Count](./5-count.py)
I wrote a script that counts the number of documents in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 5-count.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
simontagbor@ubuntu:~/0x01$
```

### [6. Update](./6-update.py)
I wrote a script that adds a new attribute to a document in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 6-update.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
simontagbor@ubuntu:~/0x01$

simontagbor@ubuntu:~/0x01$ cat 4-match | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
```

### [7. Delete by match](./7-delete.py)
I wrote a script that deletes all documents with `name="Holberton School"` in a collection.

#### Output
```
simontagbor@ubuntu:~/0x01$ cat 7-delete.py | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye

simontagbor@ubuntu:~/0x01$ cat 4-match | mongo
MongoDB shell version v4.2.6
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
bye
simontagbor@ubuntu:~/0x01$
```

