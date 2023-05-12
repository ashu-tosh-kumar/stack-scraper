# Stack Scraper

Stack Scraper is a sample repository showcasing how to write impeccably clean code that
will save your sanity. It is in correspondence to my Medium article [How to Write
Impeccably Clean Code That Will Save Your Sanity?](https://)

Stack-Scraper contains one scrapper that gets triggered every day and scrapes questions
and answers from Stack Overflow. We are making following assumptions about Stack
Overflow.

- Stack Overflow is a single page website.
- All the questions are numbered in integers.
- Each question has only one answer which could be accepted or not.

## Architecture

- All the scraped data is stored in the Cassandra database.
- Stack-Scraper provides one REST endpoint to fetch the scraped data stored in the
  database by a given question number.

Please note that this is not a working project but only to showcase the ideas discussed
in aforementioned article.

## Repository Structure

```text
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── src
│    ├── apis
│    │    └── question_no.py
│    ├── constants
│    │    └── api_constants.py
│    ├── db_wrappers
│    ├── domain_models
│    │    ├── domain_enums.py
│    │    └── domain_models.py
│    ├── external_sources
│    │    ├── apis
│    │    └── scrappers
│    ├── initializer.py
│    ├── main.py
│    ├── scripts
│    ├── secret.py
|    ├── config.py
│    └── utils
└── test
    └── src
        ├── apis
        ├── constants
        ├── db_wrappers
        ├── domain_models
        ├── external_sources
        │    ├── apis
        │    └── scrappers
        └── utils
```

`src/`: Notice that all the source code is under the /src folder. This is not mandatory
but would be helpful if you want to convert your project into a sharable pip package.

`apis/`: This folder contains all the domain REST endpoints (except the health check) in
the project. We can create a new file under the apis folder for each new API we add to
the project. This will help in having all the API code in one place and separate
different APIs.

`constants/`: This folder should contain all application-wide constants. It also helps
business to check any business level constants like standard responses etc. Moreover, it
makes it easy to change any value without having to worry about making same change at
multiple places. Additionally, you should not put all constants in a single file naming
constants.py as overtime it would grow to be a mess of its own. Instead try to create
multiple files each containing a set of related constants. For example: stack_xpaths.py
to store all xpaths for scraping, api_constants.py to store API level constants like
HEALTH_RESPONSE.

`db_wrappers/`: This folder contains all the database models and wrappers to allow
interaction with the database.

`domain_models`: This folder contains all the pydantic based models and enum classes.

`external_sources`: This folder contains all the scrappers and/or external API
integrations. Our scrapper for Stack Overflow would reside under
`external_sources/scrappers`.

`utils`: This folder contains all the utility code. Please note not to dump all
utility functions in a single utility files. Instead try to a create logical grouping
with each file containing each group.

`test`: This folder contains all the test files. Note that `test` directory follows the
same folder hierarchy as the code under `src`. This helps in maintaining test files of a
large number of modules in a big project. Also, it aids in finding test file for a given
module easily as for a given file `dir1/dir2/dir3/file.py`, you know that the respective
test file would be `test/dir1/dir2/dir3/test_file.py`.
