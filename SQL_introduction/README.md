# SQL Introduction

This project aims to provide a foundational understanding of SQL (Structured Query Language) and MySQL through practical exercises. By completing these tasks, you'll gain proficiency in fundamental database operations, from creating and manipulating databases to querying and modifying data. Each script is designed to reinforce key concepts such as database creation, table management, data insertion, and retrieval using MySQL commands.

By the end of this project, you'll be equipped to explain the basics of databases, understand relational database management systems, and confidently execute SQL queries—all essential skills for anyone diving into the realm of data management and backend development.

### General
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s `MySQL`
- How to create a database in `MySQL`
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are subqueries
- How to use `MySQL functions`

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be executed on `Ubuntu 20.04 LTS` using `MySQL 8.0` (`version 8.0.25`)
- All your files should end with a new line
- All your `SQL` queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All `SQL` keywords should be in uppercase (`SELECT`, `WHERE`…)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## More Info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

## Connect to your MySQL server:

```
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
...
mysql> quit
Bye
```

## Using MySQL with Docker

### 1. Downloading the MySQL Image

1. **Download the MySQL image from Docker Hub**:

   ```
   docker pull mysql:latest
   ```
2. Verifying Docker Images
Verify that the image has been downloaded:

```
docker images
```
3. Running a MySQL Container
Start a MySQL container:

```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
4. Verify the Container is Running
Check the running containers:

```
docker ps
```
5. Accessing the MySQL Container
Access the MySQL container:

```
docker exec -it some-mysql bash
```
Check MySQL status within the container (if needed):

```
mysqladmin -uroot -p status
```
Log into MySQL:

```
mysql -uroot -p
Enter the password (root in this case).
```

6. Running SQL Scripts
Exit MySQL prompt:

```
quit
```
Copy your SQL script into the container:

```
docker cp 0-list_databases.sql some-mysql:/0-list_databases.
```
Run the SQL script inside the container:

```
docker exec -it some-mysql bash
```
```
mysql -uroot -p < /0-list_databases.sql
```
Enter the password (root in this case).

7. Viewing the Databases
Log back into MySQL to view the databases:

```
mysql -uroot -p
```
Enter the password (root in this case).

Show the databases:

```
SHOW DATABASES;
```

## Tasks:

| File                   | Description                                          |
|------------------------|------------------------------------------------------|
| `0-list_databases.sql` | Lists all databases of the MySQL server              |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it doesn't exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists       |
| `3-list_tables.sql`    | Lists all tables of a specified database             |
| `4-first_table.sql`    | Creates a table `first_table` in the current database |
| `5-full_table.sql`     | Prints the full description of the table `first_table` |
| `6-list_values.sql`    | Lists all rows of the table `first_table`            |
| `7-insert_value.sql`   | Inserts a new row into the table `first_table`       |
| `8-count_89.sql`       | Displays the number of records with id = 89 in `first_table` |
| `9-full_creation.sql`  | Creates table `second_table` and adds multiple rows  |
| `10-top_score.sql`     | Lists all records of `second_table` ordered by score |
| `11-best_score.sql`    | Lists records with score >= 10 in `second_table`     |
| `12-no_cheating.sql`   | Updates the score of Bob to 10 in `second_table`     |
| `13-change_class.sql`  | Removes all records with score <= 5 in `second_table`|
| `14-average.sql`       | Computes the score average of all records in `second_table` |
| `15-groups.sql`        | Lists the number of records for each score in `second_table` |
| `16-no_link.sql`       | Lists all records of `second_table` without a name value |

_________________________
_________________________
<br><br>
Copyright (c) 2024 - Clément DEFER
