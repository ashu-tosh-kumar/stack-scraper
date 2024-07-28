# Stack Scraper

Table of Content

- [Stack Scraper](#stack-scraper)
  - [Introduction](#introduction)
  - [How to run the application?](#how-to-run-the-application)
  - [Architecture](#architecture)
  - [Repository Structure](#repository-structure)

## Introduction

Stack Scraper is a sample repository showcasing how to write impeccably clean code that
will save your sanity. It is in correspondence to my Medium article published by
gitconnected: [How to Write Impeccably Clean Code That Will Save Your
Sanity](https://medium.com/gitconnected/how-to-write-impeccably-clean-code-that-will-save-your-sanity-7d0ea59d285c)

Stack-Scraper contains one scrapper that can be triggered on demand and scrapes
questions and answers from Stack Overflow. We are making the following assumptions about
Stack Overflow.

- Stack Overflow is a single page website.
- All the questions are numbered in integers.
- Each question has only one answer which could be accepted or not.

## How to run the application?

To run the application, clone the repository and run the command `python -m src.main`
from inside the repository location.

You can also use Docker to run the service using commands:

```bash
docker compose build
docker compose up -d
```

Once the application is up, you can run `curl localhost:8000/health` to confirm that the
API is working fine. You should receive a response like `{"message":"Stack Scraper at
your service","status":"SUCCESS"}`

To run the scraper, run `curl -X POST localhost:8000/stackoverflow`. If the scrappers
run, you would receive a response like `{"status":"SUCCESS"}`.

Once the scrappers run, you can try following commands to try out the
Stack Scraper.

`curl localhost:8000/stackoverflow/1` : Should return successful response

`curl localhost:8000/stackoverflow/2` : Should return successful response

`curl localhost:8000/stackoverflow/3` : Should return successful response

`curl localhost:8000/stackoverflow/4` : Should return successful response

`curl localhost:8000/stackoverflow/5` : Should return question doesn't exist response

## Architecture

- All the scraped data is stored in an in-memory database.
- Stack-Scraper provides following REST endpoints
  - [`GET`] `/health`: To check health of the application
  - [`POST`] `/stackoverflow`: To run the scrapper
  - [`GET`] `/stackoverflow/<question_no>`" To fetch a question by its number from db

Please note that this is not a working project but only to showcase the ideas discussed
in the article mentioned above.

## Repository Structure

```text
.
├── src
│   ├── apis
│   │   └── question_no.py
│   ├── config.py
│   ├── constants
│   │   ├── api_constants.py
│   │   └── mock_data.py
│   ├── db_wrappers
│   │   ├── db_models.py
│   │   └── in_memory_db.py
│   ├── domain_models
│   │   ├── domain_enums.py
│   │   └── domain_models.py
│   ├── external_sources
│   │   ├── apis
│   │   ├── external_source_base.py
│   │   ├── scrapper_tasks.py
│   │   └── scrappers
│   │       └── stack_overflow.py
│   ├── main.py
│   ├── scripts
│   │   ├── run_api.py
│   │   └── run_api.sh
│   ├── secret.py
│   └── utils
└── test
    └── src
        ├── apis
        │   └── test_question_no.py
        ├── constants
        │   └── test_api_constants.py
        ├── db_wrappers
        │   ├── test_db_models.py
        │   └── test_in_memory_db.py
        ├── domain_models
        │   ├── test_domain_enums.py
        │   └── test_domain_models.py
        ├── external_sources
        │   ├── apis
        │   ├── scrappers
        │   │   └── test_stack_overflow.py
        │   ├── test_external_source_base.py
        │   └── test_scrapper_tasks.py
        ├── test_config.py
        ├── test_main.py
        ├── test_secret.py
        └── utils
```

`src/`: Notice that all the source code is under the `src` folder. This is not mandatory
but would be helpful if you want to convert your project into a sharable pip package.

`apis/`: This folder contains all the domain REST endpoints (except the health check) in
the project. We can create a new file under the `apis` folder for each new API we add to
the project. This will help in having all the API code in one place and separate
different APIs.

`constants/`: This folder should contain all application-wide constants. It also helps
businesses to check any business-level constants like standard responses. Moreover, it
makes it easy to change any value without having to worry about making the same change
in many places. Additionally, you should not put all constants in a single file naming
constants.py as over time it would grow to be a mess of its own. Instead, try to create
many files each containing a set of related constants. For example: stack_xpaths.py
to store all xpaths for scraping, api_constants.py to store API level constants like
HEALTH_RESPONSE.

`db_wrappers/`: This folder contains all the database models and wrappers to allow
interaction with the database.

`domain_models`: This folder contains all the pydantic-based models and enum classes.

`external_sources`: This folder contains all the scrappers and/or external API
integrations. Our scrapper for Stack Overflow would live under
`external_sources/scrappers`.

`utils`: This folder contains all the utility code. Please note not to dump all
utility functions in a single utility file. Instead, try to a create logical grouping
with each file containing each group.

`test`: This folder contains all the test files. Note that the `test` directory follows
the same folder hierarchy as the code under `src`. This helps in maintaining test files
of a large number of modules in a big project. Also, it aids in finding test files for a
given module easily.
