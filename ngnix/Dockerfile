run:
	 && poetry run uvicorn app.main:app --reload

lint:
	 && poetry run ruff check .

format:
	 && poetry run ruff format .

up:
	docker-compose up --build

down:
	docker-compose down -v

test:
	cd backend && PYTHONPATH=.:.. poetry run pytest -v ../tests

requirements:
	 && poetry export -f requirements.txt --output requirements.txt --without-hashes