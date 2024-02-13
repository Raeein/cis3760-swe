#--------------------------------------------------------------------
    # ARG PYTHON_VERSION=3.12
    # FROM --platform=linux/amd64 python:${PYTHON_VERSION}-slim as base

    # RUN apt-get update -y && \
    #     apt-get install -y libmariadb-dev gcc wget gnupg

    # RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
    # RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
    # RUN apt-get update -y && apt-get install -y google-chrome-stable

    # # Prevents Python from writing pyc files.
    # ENV PYTHONDONTWRITEBYTECODE=1
    # #ENV LD_PRELOAD=/usr/lib/mariadb/libmariadb.so
    # #ENV LD_LIBRARY_PATH=/usr/lib/mariadb
    # # Keeps Python from buffering stdout and stderr to avoid situations where
    # # the application crashes without emitting any logs due to buffering.
    # ENV PYTHONUNBUFFERED=1

    # WORKDIR /app

    # # Create a non-privileged user that the app will run under.
    # # See https://docs.docker.com/go/dockerfile-user-best-practices/
    # # ARG UID=10001
    # # RUN adduser \
    # #     --disabled-password \
    # #     --gecos "" \
    # #     --home "/nonexistent" \
    # #     --shell "/sbin/nologin" \
    # #     --no-create-home \
    # #     --uid "${UID}" \
    # #     appuser

    # # Download dependencies as a separate step to take advantage of Docker's caching.
    # # Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
    # # Leverage a bind mount to requirements.txt to avoid having to copy them into
    # # into this layer.
    # RUN --mount=type=cache,target=/root/.cache/pip \
    #     --mount=type=bind,source=requirements.txt,target=requirements.txt \
    #     python -m pip install -r requirements.txt


    # # Switch to the non-privileged user to run the application.
    # #USER appuser

    # # Copy the source code into the container.
    # COPY . .
    # CMD ["python3", "main.py"]
#--------------------------------------------------------------------


# 
FROM node:alpine

# Copy package.json and package-lock.json to the image
# We need them to build the dependencies for our project

RUN npm i npm@latest -g
COPY package.json package.json
COPY package-lock.json package-lock.json

# Run `npm ci` to install project dependencies
RUN npm ci

# Set environment variables
ENV CI=true
ENV PORT=3000

# Copy the entire project directory to the image
COPY . .

# Default command to start the app
CMD [ "npm", "start" ]
