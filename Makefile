FASTAPI_SERVICES := text_service summary_service session_service ptt_service

up:
	docker-compose up --build

up_d:
	docker-compose up --build -d

down:
	docker-compose down -v

logs:
	docker-compose logs -f

tree:
	tree -I 'frontend'

lint_all:
	for service in $(FASTAPI_SERVICES); do \
		if [ -d backend/$$service ]; then \
			echo "Linting $$service..."; \
			( cd backend/$$service && poetry run ruff check . ); \
		else \
			echo "Skipping $$service, folder not found"; \
		fi; \
	done

format_all:
	for service in $(FASTAPI_SERVICES); do \
		if [ -d backend/$$service ]; then \
			echo "Formatting $$service..."; \
			( cd backend/$$service && poetry run ruff format . ); \
		else \
			echo "Skipping $$service, folder not found"; \
		fi; \
	done