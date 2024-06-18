# SQL More Queries
This project is designed to deepen your understanding of SQL (Structured Query Language) by working through more complex queries and database management tasks. You will gain practical experience with user privileges, creating users, managing database constraints, and executing advanced SQL queries. By the end of this project, you will be able to handle a variety of SQL tasks with confidence and precision.


## More Info
Comments for your SQL file:
```
$ cat 0-privileges.sql
```
-- List all privileges of the MySQL server
```
SHOW GRANTS FOR 'root'@'localhost';
```
Install MySQL 8.0 on Ubuntu 20.04 LTS
```
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```
Connect to your MySQL server:
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
1. **Downloading the MySQL Image**<br>

```
docker pull mysql:latest
```
**Verifying Docker Images:**<br>

```
docker images
```
**Running a MySQL Container:**<br>

```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
```
**Verify the Container is Running:**<br>

```
docker ps
```
**Accessing the MySQL Container:**<br>

```
docker exec -it some-mysql bash
```
**Check MySQL status within the container (if needed):**<br>
```
mysqladmin -uroot -p status
```
**Log into MySQL:**

```
mysql -uroot -p
```
**Enter the password (root in this case).**

```
quit
```
**Copy your SQL script into the container:**

```
docker cp 0-privileges.sql some-mysql:/0-privileges.sql
```
**Run the SQL script inside the container:**

```
docker exec -it some-mysql bash
```
```
mysql -uroot -p < /0-privileges.sql
```
**Enter the password (root in this case).**

**Viewing the Databases:**<br>
Log back into MySQL to view the databases:

```
mysql -uroot -p
```


**Show the databases:**

```
SHOW DATABASES;
```
## DATA-Persitence with Docker-Volume 
1. **Create Docker Volume:**
   - Use `docker volume create <volume_name>` to create a new Docker volume.
     Example: `docker volume create mysql_data`

2. **Run MySQL Container with Volume Mount:**
   - Start a MySQL container with the `-v` or `--volume` option to mount the volume.
     Example:
     ```bash
     docker run -d \
       --name mysql-container \
       -e MYSQL_ROOT_PASSWORD=my-secret-pw \
       -v mysql_data:/var/lib/mysql \
       mysql:latest
     ```

3. **Verify Volume Mounting:**
   - Use `docker inspect <container_id_or_name>` to check volume mounting details.
     Example: `docker inspect mysql-container`

4. **Conclusion:***
   - After running the container and verifying the volume mount, the container is linked to the Docker volume `mysql_data`.

## Tasks
| File                   | Description                                          |
|------------------------|------------------------------------------------------|
| `0-privileges.sql`                       | Lists all privileges of the MySQL server                     |
| `1-create_user.sql`                      | Creates a new user with specific privileges                  |
| `2-create_read_user.sql`                 | Creates a user with read-only access to a specific database  |
| `3-force_name.sql`                       | Forces a table column to be NOT NULL                         |
| `4-never_empty.sql`                      | Ensures a column always has a default value                  |
| `5-unique_id.sql`                        | Creates a table with a unique identifier                     |
| `6-states.sql`                           | Lists all states in a specific database                      |
| `7-cities.sql`                           | Lists all cities in a specific database                      |
| `8-cities_of_california_subquery.sql`    | Lists all cities in California using a subquery              |
| `9-cities_by_state_join.sql`             | Lists all cities by state using a JOIN                       |
| `10-genre_id_by_show.sql`                | Retrieves genre ID for each show                             |
| `11-genre_id_all_shows.sql`              | Retrieves genre ID for all shows                             |
| `12-no_genre.sql`                        | Lists all shows with no genre assigned                       |
| `13-count_shows_by_genre.sql`            | Counts the number of shows per genre                         |
| `14-my_genres.sql`                       | Lists genres associated with a specific user                 |
| `15-comedy_only.sql`                     | Lists all comedy shows                                       |
| `16-shows_by_genre.sql`                  | Lists all shows grouped by genre                             |

<br><br>
Copyright (c) 2024 - Clément DEFER