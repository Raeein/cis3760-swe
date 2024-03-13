stages:
  - build
  - lint
  - test

build-java:
  stage: build
  image: maven:3.8.4-openjdk-17
  script:
    - cd spring
    - mvn clean install -DskipTests
  rules:
    - when: always


build-python:
  stage: build
  image: python:3.12
  script:
    - cd scraper
    - pip install poetry==1.7.1
    - poetry install # Doesnt build anything, just installs the dependencies
  rules:
    - when: always

python-lint:
  stage: lint
  image: python:3.12
  script:
    - cd scraper
    - pip install poetry==1.7.1
    - poetry install
    - poetry run flake8
  rules:
    - when: always

java-lint:
  stage: lint
  image: maven:3.8.4-openjdk-17
  script:
    - cd spring
    - mvn checkstyle:check
  rules:
    - when: always

react-lint:
  stage: lint
  image: node:16
  script:
    - cd react
    - npm install
    - npx eslint .
  rules:
    - when: always
  allow_failure: false
python-test:
  stage: test
  image: python:3.12
  script:
    - cd scraper
    - apt-get update && apt-get install -y firefox-esr
    - chmod +x install.sh && ./install.sh
    - pip install poetry==1.7.1
    - poetry install
    - poetry run pytest --cov scraper
  rules:
    - when: always
  allow_failure: false

java-test:
  stage: test
  image: maven:3.8.4-openjdk-17
  script:
    - echo "Running Java Spring tests"
    - cd spring
    - mvn test
  rules:
    - when: always
  allow_failure: false
