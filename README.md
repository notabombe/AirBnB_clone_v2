![HBNB](http://imgur.com/JBCMHDP.png)

# AirBnB Clone Version 2.0

: python BaseModel Class, unittests, python CLI, & web static, MySQL

### Synopsis
The objective of the AirBnB Clone project is to learn the fundamental concepts to building a web application similar to AirBnB. AirBnB. AirBnB is an online marketplace and hospitality service, enabling people to lease or rent short-term lodging.

This portion of the project is the first step towards building the full web application; it includes a command interpreter (accessed through a console) for manipulating data and Holberton AirBnB (`HBNB`) objects.

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End.

## Environment

* __OS:__ Ubuntu 14.04 LTS
* __Database__ MySQL 5.7.8-rc
* __language:__ Python 3.4.3
* __style:__ PEP 8 (v. 1.7.0)

<img src="https://github.com/johncoleman83/AirBnB_clone/blob/master/dev/hbnb_step5.png" />

## Testing

#### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

* `python3 -m unittest discover -v ./tests/`

The bash script `init_test.sh` executes all these tests:

  * checks `pep8` style

  * runs all unittests

  * runs all w3c_validator tests

  * cleans up all `__pycache__` directories and the storage file, `file.json`

**Usage:**

```
$ ./dev/init_test.sh
```

#### CLI Interactive Tests

This project uses python library, `cmd` to run tests in an interactive command
line interface.  To begin tests with the CLI, run this script:

```
$ ./console.py
```

* For a detailed description of all tests, run these commands inside the
custom CLI:

```
$ ./console.py
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG]
        ARG = Class Name
        SYNOPSIS: Creates a new instance of the Class from given input ARG
        EXAMPLE: create City
                 City.create()
```

* Tests in the CLI may also be executed with this syntax:

  * **destroy:** `<class name>.destroy(<id>)`

  * **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

  * **update with dictionary:** `<class name>.update(<id>, <dictionary representation>)`

#### Environmental variables

* `HBNB_ENV`: running environment. 
* `HBNB_MYSQL_USER`: the username
* `HBNB_MYSQL_PWD`: the password
* `HBNB_MYSQL_HOST`: the hostname
* `HBNB_MYSQL_DB`: the database name 
* `HBNB_TYPE_STORAGE`: the type of storage used.

#### Continuous Integration

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Authors

* MJ Johnson, [@mj31508](https://github.com/mj31508)
* David John Coleman II, [davidjohncoleman.com](http://www.davidjohncoleman.com/)
* Jared Heck, [@jarehec](https://github.com/jarehec)
* Spencer Cheng [@spencerhcheng](https://github.com/spencerhcheng)

## License

Public Domain, no copyright protection. Feedback and contributors welcome. Please reach out to any of the authors.
