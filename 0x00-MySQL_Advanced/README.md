# 0x00. MySQL advanced
#### ` Back-end - Databases ` ` SQL ` ` MySQL `

## Leaning Outcomes
In this project, I learned how to use MySQL in a more advanced way.
- I learned about creating tables with constraints
- I Implemented stored procedures and functions in MySQL
- I learned how to create and trigger SQL events
- I learned how to create views in MySQL

## Tasks

### [0. We are all unique!](./0-uniq_users.sql)
I this task, I wrote a SQL script that creates a table `users` following these requirements:
- `id` INT
    - unique, can't be null and is a primary key
- `email` VARCHAR(256)
    - can't be null and must be unique
- `name` VARCHAR(256)
    - can't be null

#### Output
```
simontagbor@ubuntu:~/$ cat 0-uniq_users.sql | mysql -hlocalhost -uroot -p
Enter password:
simontagbor@ubuntu:~/$ cat 0-uniq_users.sql | mysql -hlocalhost -uroot -p
Enter password:
simontagbor@ubuntu:~/$ echo 'INSERT INTO users (email, name) VALUES ("simom@tagbor.com", "Simon Tagbor");' | mysql -hlocalhost -uroot -p holberton
Enter password:
simontagbor@ubuntu:~/$ echo 'INSERT INTO users (email, name) VALUES ("bob@john.com", "Bob John");' | mysql -hlocalhost -uroot -p holberton	
Enter password:
simontagbor@ubuntu:~/$ echo 'INSERT INTO users (email, name) VALUES ("simon@tagbor", "Simon Tagbor");' | mysql -hlocalhost -uroot -p holberton
Enter password:
ERROR 1062 (23000) at line 1: Duplicate entry 'simon@tagbor' for key 'email'

simontagbor@ubuntu:~/$ echo 'SELECT * FROM users;' | mysql -hlocalhost -uroot -p holberton
Enter password:
id  email               name
1   simon@tagbor.com   Simon Tagbor
2   bob@john.com        Bob John
simontagbor@ubuntu:~/$
```

### [1. In and not out](./1-country_users.sql)


