# Setup Python and Pip
FROM python:3.11.10-bullseye

# Poetry
# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=2.0.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache \
    PYTHONPATH=/stack-scraper

# install system packages, setup poetry
RUN apt-get update \
    && apt-get -qq clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools poetry==${POETRY_VERSION}

# Setup working directory
WORKDIR /stack-scraper

# Copy project files into the image
COPY pyproject.toml poetry.lock ./

# Install Dependencies
# First write to a temp file to avoid reading and writing to a file at the same time:
# https://www.shellcheck.net/wiki/SC2094
RUN $POETRY_VENV/bin/poetry self add poetry-plugin-export \
    && $POETRY_VENV/bin/poetry export -f requirements.txt --without-hashes > requirements.tmp \
    && mv requirements.tmp requirements.txt \
    && pip install --no-input --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./src stack-scraper/src

# Provide access to script files
RUN chmod -R 755 stack-scraper/src/scripts

# Expose the application port
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["bash"]