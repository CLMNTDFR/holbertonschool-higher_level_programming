# Python Object Relational Mapping Project

## Introduction
In this project, we explore the integration of two powerful worlds: Databases and Python. <br>Initially, we use the MySQLdb module to connect to a MySQL database and execute SQL queries. Subsequently, we utilize SQLAlchemy, an Object Relational Mapper (ORM), to abstract the storage concerns and focus on manipulating Python objects without directly writing SQL queries. <br>The primary goal is to make database interactions more intuitive and flexible, emphasizing the operations on objects rather than on the database itself.

## Requirements
- Before you start, ensure your MySQL server is version 8.0.
- Below are the installation steps for MySQL 8.0 on Ubuntu 20.04:

```sh
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```

## To connect to your MySQL server:
```
$ sudo mysql
mysql> quit
Bye
```

## Install the necessary Python modules:

```
# MySQLdb module version 2.0.x
$ sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
$ sudo pip3 install mysqlclient

# SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
```

## Learning Objectives

- Connect to a MySQL database from a Python script.
- Perform SQL SELECT and INSERT operations from Python.
- Understand the principles of Object-Relational Mapping (ORM).
- Map Python classes to MySQL tables using SQLAlchemy.

## Tasks
| File                   | Description                                          |
|------------------------|------------------------------------------------------|
| `0-select_states.py` | Lists all states from the database |
| `1-filter_states.py` | Lists all states with a name starting with 'N' |
| `2-my_filter_states.py` | Lists states with a user-specified name |
| `3-my_safe_filter_states.py` | Lists states with a user-specified name (SQL injection free) |
| `4-cities_by_state.py` | Lists all cities from a state |
| `5-filter_cities.py` | Lists all cities with a user-specified name |
| `model_state.py` | Model for the State class |
| `7-model_state_fetch_all.py` | Fetches all State objects |
| `8-model_state_fetch_first.py` | Fetches the first State object |
| `9-model_state_filter_a.py` | Filters State objects containing the letter 'a' |
| `10-model_state_my_get.py` | Gets a state by name |
| `11-model_state_insert.py` | Inserts a new State object |
| `12-model_state_update_id_2.py`| Updates the State object with id 2 |
| `13-model_state_delete_a.py` | Deletes State objects containing the letter 'a' |
| `14-model_city_fetch_by_state.py` | Fetches cities by state |
| `model_city.py` | Model for the City class |

<br><br>
Copyright (c) 2024 - Clément DEFER