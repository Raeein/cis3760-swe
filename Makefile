THIS_FILE := $(lastword $(MAKEFILE_LIST))

COMPOSE_FILE := compose.yml
TEST_COMPOSE_FILE := test.yml

.PHONY: all help build up down restart clean test log
help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'
build:
	docker compose -f  $(COMPOSE_FILE) build $(c)
up:
	docker compose -f  $(COMPOSE_FILE) up -d $(c)
down:
	docker compose -f  $(COMPOSE_FILE) down $(c)
restart:
	docker compose -f  $(COMPOSE_FILE) down -v $(c)
	docker compose -f  $(COMPOSE_FILE) up --build $(c)
test:
	docker compose -f $(TEST_COMPOSE_FILE) up --build $(c)
	@echo "Running tests..."
	docker compose -f $(TEST_COMPOSE_FILE) down
