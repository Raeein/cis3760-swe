ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim as base

ENV POETRY_NO_INTERACTION=1 \
      PYTHONFAULTHANDLER=1 \
      PYTHONUNBUFFERED=1 \
      PIP_DEFAULT_TIMEOUT=100 \
      POETRY_VIRTUALENVS_CREATE=false \
      POETRY_CACHE_DIR='/var/cache/pypoetry' \
      POETRY_HOME='/usr/local' \
      POETRY_VERSION=1.7.1

RUN apt-get update -y && \
    apt-get install -y libmariadb-dev gcc firefox-esr cron

# Only way that worked dont ask me why <3
RUN pip install poetry==$POETRY_VERSION

COPY geckodriver-v0.34.0-linux-aarch64.tar.gz /usr/bin/
RUN tar -xvzf /usr/bin/geckodriver-v0.34.0-linux-aarch64.tar.gz -C /usr/bin/
RUN mv /usr/bin/geckodriver /usr/bin/geckodriver-arm
RUN chmod +x /usr/bin/geckodriver-arm

COPY geckodriver-v0.34.0-linux64.tar.gz /usr/bin/
RUN tar -xvzf /usr/bin/geckodriver-v0.34.0-linux64.tar.gz -C /usr/bin/
RUN chmod +x /usr/bin/geckodriver
RUN rm /usr/bin/geckodriver-v0.34.0-linux64.tar.gz

WORKDIR /app

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --no-root --no-dev

COPY . .

# CMD ["poetry", "run", "python", "main.py"]
CMD ["bash", "setup-cron.sh"]
