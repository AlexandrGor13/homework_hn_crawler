.ONESHELL:

.PHONY: help
help: ## Вывод справки
	@egrep '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: up
up: ## Запуск контейнера
	@docker compose up -d --build

.PHONY: down
down: ## Остановка контейнера
	@docker compose down

.PHONY: bash
bash: ## Перейти в контейнер
	@docker compose exec app /bin/bash

.PHONY: ps
ps: ## Просмотр информации о контейнере
	@docker compose ps

.PHONY: test
test: ## Запуск тестов
	@pytest /tests -v



