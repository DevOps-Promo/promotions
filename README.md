<img align="center" src="https://github.com/DevOps-Promo/promotions/blob/master/assets/promo.png" alt="Promo" width="900">
<h1 align="center">
Promotions Resource
</h1>
<h4 align="center"> <strong>A RESTful microservice based on a resource from an eCommerce application </strong></h3>

<p align="center">
    <a href="https://travis-ci.org/DevOps-Promo/promotions">
        <img src="https://img.shields.io/travis/DevOps-promo/promotions/master?style=flat-square"
             alt="travis">
      </a>
    <a href="https://codecov.io/gh/DevOps-Promo/promotions">
    <img src="https://img.shields.io/codecov/c/github/DevOps-promo/promotions/master?style=flat-square"
         alt="codecov">
    </a>
    <a href="https://github.com/devops-promo/promotions/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/devops-promo/promotions.svg?style=flat-square"
         alt="contributors">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0">
    <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square"
         alt="license">
    </a>
</p>

<p align="center">
  <a href="#introduction">Introduction</a> «
  <a href="#overview">Overview</a> «
  <a href="#setup">Setup</a> «
  <a href="#attributes">Attributes</a> «
  <a href="#functions">Functions</a> «
  <a href="#whats-featured-in-the-project">Featured</a> «
  <a href="#running-the-tests">Tests</a> «
  <a href="#license">License</a>
</p>


##  Introduction 👋

#### The promotions resource is a representation of a special promotion or sale that is running against a product or perhaps the entire store. Some examples are "buy 1 get 1 free", "20% off", etc. Discount promotions usually apply for a given duration (e.g., sale for 1 week only).

<br>


##  Overview 👀

This project's `/service` folder contains a file for the `Promotion` model and a `service.py` file for promotions service. The `/tests` folder has test case code for testing the model and the service separately. 

<br>

##  Setup 💾

To run this project, clone this repository and 
[install vagrant virtual machine](https://www.vagrantup.com/downloads.html)
. Next, initialize a vagrant enviroment using `vagrant up`. Then do:

```bash
vagrant ssh
cd /vagrant
nosetests
honcho start
```

<br>

##  Attributes ⚙️

The `Promotion` Model contains the following attributes: <br>
* `"name"` <br>
* `"description"` <br>
* `"start_date"`<br>
* `"end_date"`<br>


<br>

##  Functions 🛠

The following lists the RESTful routes:
```
Endpoint           Methods  Rule                                Description
----------------   -------  ----------------------------        -------------------------
index              GET      /                            

create_promotions  POST     /promotions                         create a promotion object and adds it to the database
get_promotions     GET      /promotions/<promotion_id>          return the information for a specified promotion
update_promotions  PUT      /promotions/<promotion_id>          edit and save changes to a promotion
delete_promotions  DELETE   /promotions/<promotion_id>          remove a promotion from the database
list_promotions    GET      /promotions                         list all promotions in the databas
search_promotions  GET      /promotions/<params>                search the database for promotions that match the query parameters
cancel_promotions  GET      /promotions/cancel/<promotion_id>   end a promotion early

```

<br>

##  What's Featured in the Project? ❓

The project contains the following:

```text
.github/            - contains a template for github issues
assets/             - contains image files

service/            - service python package
├── static/         - conatains web UI files
├── __init__.py     - package initializer
├── models.py       - module with business models
└── service.py      - module with service routes

tests/              - test cases package
├── __init__.py     - package initializer
├── test_models.py  - test suite for busines models
└── test_service.py - test suite for service routes

.coveragerc         - settings file for code coverage options
.gitignore          - this will ignore vagrant and other metadata files
.travis.yml         - travis configuration file
LICENSE             - Apache 2.0
Procfile            - a command to run by the container
README.md           - repo documentation file
Vagrantfile         - Vagrant file that installs requirements to the VM
codecov.yml         - codecov configuration file
config.py           - configuration parameters
dot-env-example     - copy to .env to use environment variables
manifest.yml        - ibm cloud foundry configuration file
requirements.txt    - list if Python libraries required by your code
runtime.txt         - python version to be used at runtime
setup.cfg           - nosetests configuration file
```

<br>

##  Running the Tests 🔩

Run the tests using `nosetests` and `coverage`

    $ nosetests
    $ coverage report -m --include=server.py

Nose is configured to automatically include the flags `--rednose --with-spec --spec-color --with-coverage` so that red-green-refactor is meaningful. If you are in a command shell that supports colors, passing tests will be green while failing tests will be red.

<br>

## License 📃 
Apache 2.0

---
<sub> This repository is part of the NYU class **CSCI-GA.2810-001: DevOps and Agile Methodologies** taught by John Rofrano, Adjunct Instructor, NYU Curant Institute, Graduate Division, Computer Science.</sub>
