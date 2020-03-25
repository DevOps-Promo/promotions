<img src="https://github.com/DevOps-Promo/promotions/blob/savannahs_branch/assets/promo.png" alt="Promo" width="900">

# Promotions

[![Build Status](https://travis-ci.org/DevOps-Promo/promotions.svg?branch=savannahs_branch)](https://travis-ci.org/DevOps-Promo/promotions)
[![Codecov](https://img.shields.io/codecov/c/github/DevOps-Promo/promotions.svg)]()

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
<br>
<br>


## Introduction

#### The promotions resource is a representation of a special promotion or sale that is running against a product or perhaps the entire store. Some examples are "buy 1 get 1 free", "20% off", etc. Discount promotions usually apply for a given duration (e.g., sale for 1 week only).



## Overview

This project's `/service` folder contains a file for the `Promotion` model and a `service.py` file for promotions service. The `/tests` folder has test case code for testing the model and the service separately. 


## Setup

To run this project, clone this repository and 
[install vagrant virtual machine](https://www.vagrantup.com/downloads.html)
. Next, initialize a vagrant enviroment using `vagrant up`. Then do:

```bash
vagrant ssh
cd /vagrant
nosetests
flask run -h 0.0.0.0
```


## Functions

The following lists the RESTful routes:
```
Endpoint           Methods  Rule                          Description
----------------   -------  ----------------------------  -------------------------
index              GET      /                            

create_promotions  POST     /promotions                   create a promotion object and adds it to the database
get_promotions     GET      /promotions/<promotion_id>    return the information for a specified promotion
update_promotions  PUT      /promotions/<promotion_id>    edit and save changes to a promotion
delete_promotions  DELETE   /promotions/<promotion_id>    remove a promotion from the database
list_promotions    GET      /promotions                   list all promotions in the databas
search_promotions  GET      /promotions/<params>          search the database for promotions that match the query parameters
cancel_promotions  GET      /promotions/<promotion_id>    end a promotion early

```

## Attributes

The `Promotion` Model contains the following attributes: <br>
* `"name"` <br>
* `"description"` <br>
* `"start_date"`<br>
* `"end_date"`<br>


## What's Featured in the Project?

The project contains the following:

```text
.coveragerc         - settings file for code coverage options
.gitignore          - this will ignore vagrant and other metadata files
dot-env-example     - copy to .env to use environment variables
requirements.txt    - list if Python libraries required by your code
config.py           - configuration parameters

assets/             - image files

service/            - service python package
├── __init__.py     - package initializer
├── models.py       - module with business models
└── service.py      - module with service routes

tests/              - test cases package
├── __init__.py     - package initializer
├── test_models.py  - test suite for busines models
└── test_service.py - test suite for service routes

Vagrantfile         - Vagrant file that installs Python 3 and PostgreSQL
```



## Running the Tests

Run the tests using `nosetests` and `coverage`

    $ nosetests
    $ coverage report -m --include=server.py

Nose is configured to automatically include the flags `--rednose --with-spec --spec-color --with-coverage` so that red-green-refactor is meaningful. If you are in a command shell that supports colors, passing tests will be green while failing tests will be red.

---
<sub> This repository is part of the NYU class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by John Rofrano, Adjunct Instructor, NYU Curant Institute, Graduate Division, Computer Science.</sub>
