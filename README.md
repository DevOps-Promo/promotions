# Promotions

##### The promotions resource is a representation of a special promotion or sale that is running against a product or perhaps the entire store. Some examples are "buy 1 get 1 free", "20% off", etc. Discount promotions usually apply for a given duration (e.g., sale for 1 week only).

## Overview

This project template contains starter code for your class project. The `/service` folder contains your `models.py` file for your model and a `service.py` file for your service. The `/tests` folder has test case starter code for testing the model and the service separately. All you need to do is add your functionality. You can use the [lab-flask-rest](https://github.com/nyu-devops/lab-flask-rest)
for code examples.

## Setup

run command  ``` vagrant up && vagrant ssh ``` to initiate development environment

## Contents

The project contains the following:

```text
dot-env-example     - copy to .env to use environment variables
config.py           - configuration parameters

service/            - service python package
├── __init__.py     - package initializer
├── models.py       - module with business models
└── service.py      - module with service routes

tests/              - test cases package
├── __init__.py     - package initializer
├── test_models.py  - test suite for busines models
└── test_service.py - test suite for service routes
```

This repository is part of the NYU class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by John Rofrano, Adjunct Instructor, NYU Curant Institute, Graduate Division, Computer Science.
