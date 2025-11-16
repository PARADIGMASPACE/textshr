BACKEND_FAST_API_DIR=backend/text_service/
BACKEND_SPRING_DIR=backend/scheduler_service/

up:
	docker-compose up -d

down:
	docker-compose down

test:
	cd backend/text_service && python -m pytest

logs:
	docker-compose logs -f

tree:
	tree -I 'frontend'

requirements:
	cd $(BACKEND_FAST_API_DIR) && poetry export -f requirements.txt --output requirements.txt --without-hashes

lint:
	cd $(BACKEND_FAST_API_DIR) && poetry run ruff check .

format:
	cd $(BACKEND_FAST_API_DIR) && poetry run ruff format .