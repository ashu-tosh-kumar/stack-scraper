# Setup Python and Pip
FROM python:3.11.3-bullseye
RUN pip install --upgrade pip
RUN pip install poetry

# Setup system packages
RUN apt-get update && apt-get -y upgrade

# Setup working directory
WORKDIR /stack-scraper

# Copy code
COPY ./src/ /stack-scraper/src
COPY ./pyproject.toml/ /stack-scraper/pyproject.toml
COPY ./poetry.lock/ /stack-scraper/poetry.lock

# Setup python packages
RUN poetry export -f requirements.txt >>requirements.txt
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Provide access to script files
RUN chmod -R 777 src/scripts

# Setup the application
EXPOSE 8000
ENV PYTHONPATH=/stack-scraper
ENTRYPOINT ["bash"]
