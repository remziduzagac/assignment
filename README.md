# Code Assignment Project
This is a coding assignment implementation that provides a simple CRUD API for property listings.
## Prerequisites
In order to run this project you will need [venv](https://docs.python.org/3/library/venv.html) and [SQLite](https://www.sqlite.org/index.html).<br />
**Note:** Project tested via Python 3.9.6
## Installation
### Create Environment
First navigate to project root.
```shell
$ cd <path to project>
```
Then create virtual environment using venv (if it is not already exists).
```shell
$ python3 -m venv venv
```
then activate it via;
```shell
$ source venv/bin/activate
(venv) $
```
Now you can install required packages.
```shell
(venv) $ pip install -r requirements.txt
```
Next we need to create required tables and populate mock data. <br />
First delete db if exists;
```shell
(venv) $ rm -f api.db
```
Then create new db with mock data using;
```shell
(venv) $ sqlite3 -init ./sql/prep.sql api.db .quit
```

### Run the Tests
Just run pytest at the project root
```shell
(venv) $ pytest
```

### Run the Project
In order to run the project run following command;
```shell
(venv) $ python -m uvicorn app.main:app --reload 
```
Now you can access project via following URLS; <br />
Project: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) <br />
Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) <br />
Redoc UI: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) <br />

## Module Overview
| **Module / Folder** | **Description**                                                                                                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| sql                 | SQL scripts                                                                                                                                                                                                 |
| app                 | Application main module                                                                                                                                                                                     |
| app.core            | Generic codes which used by other modules such as configs and base implementations                                                                                                                          |
| app.controller      | Methods handles HTTP API requests                                                                                                                                                                           |
| app.model           | Model classes                                                                                                                                                                                               |
| app.repository      | Repository classes which handles custom db operations.<br/> **Note:** Repositories only handles model specific operations. <br /> Generic CRUD operations handled via classes resides in app.core.db module |
| app.schema          | pydantic schemas which used for validations                                                                                                                                                                 |
| app.test            | Unit tests for API Tests                                                                                                                                                                                    |
| app/main.py         | Application entry point                                                                                                                                                                                     |