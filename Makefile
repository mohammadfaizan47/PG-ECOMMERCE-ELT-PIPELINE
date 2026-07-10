# ============================================
# Production-Grade E-Commerce ELT Pipeline
# Makefile — common commands shortcut
# ============================================

# Docker/Airflow commands
up:
	docker compose up -d

down:
	docker compose down
	

restart:
	docker compose restart

logs:
	docker compose logs -f

ps:
	docker compose ps

# Python environment
install:
	pip install -r requirements.txt

# Testing
test:
	pytest tests/ -v

test-coverage:
	pytest tests/ -v --cov=tasks --cov-report=term-missing

# Git shortcuts
status:
	git status

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +