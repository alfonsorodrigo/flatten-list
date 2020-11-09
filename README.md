# Flatten List API

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Getting started

Make sure you have installed.

- [Python 3.7+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/)

## Installation

Setup your environment with:

```sh
git clone git@github.com:alfonsorodrigo/flatten-list.git
cd flatten-list
docker build .
docker-compose build
```

## Run locally

it is important to execute the commands in the following order

To start the database, execute:

```sh
docker-compose run suggestic_app sh -c "python database_setup.py"
```

To start the application, execute:

```sh
docker-compose up
```

To run the tests, execute:

```sh
docker-compose run suggestic_app sh -c "python ./tests/test_flatten.py"
```
