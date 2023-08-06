# Run command
make:
	@python3 main.py

# Dockerization command
image:
	@echo "Docker build image"

# Initialization command
init:
	@chmod +x ./scripts/bash/init.sh
	@./scripts/bash/init.sh

# Utils commands
# Add main.py, all src all files without folders __pycache__
hot:
	@find | entr -c python3 src/main.py

upgrade-venv:
	@python3 -m venv --upgrade-deps .