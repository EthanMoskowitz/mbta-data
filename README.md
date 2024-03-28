
# MBTA-DATA

The MBTA Data Analyzer is a Python tool for analyzing data from the Massachusetts Bay Transportation Authority (MBTA) subway system. It's designed for developers, data analysts, and commuters interested in understanding subway routes, stops, and connections to provide insight into the MBTA subway system.

## Resources Used

 - [Requests](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
 - [Swagger](https://api-v3.mbta.com/docs/swagger/index.html#/)
 - [Pytest](https://docs.pytest.org/en/8.0.x/index.html)


## Tech Stack

**Language:** Python

**API Interaction:** Requests

**Testing:** Pytest

**Other Libraries:** Dotenv, sys, os, io

**Development Environment:** Visual Studio Code, Git

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`


## Instructions

### With Python

Install dependencies

```bash
  pip install -r requirements.txt
  or
  pip3 install -r requirements.txt --break-system-packages
```

Running the code

```bash
  python main.py
  or
  python3 main.py
```

### With Make

Install dependencies

```bash
  make init
```

Running the code

```bash
  make run
```

Clearing cache

```bash
  make clean
```

## Demo

Insert gif or link to demo


## Running Tests

### With Pytest

To run tests, run the following command

```bash
  pytest test
```

### With Make

To run tests, run the following command

```bash
  make tests
```


## Documentation

[Documentation](https://linktodocumentation)


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@EthanMoskowitz](https://www.github.com/EthanMoskowitz)

