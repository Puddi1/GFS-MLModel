# make:
# 	@find ./src | entr -c python3 src/main.py

make:
	@python3 src/main.py

image:
	@echo "Docker build image"

init:
	@python3 -m venv .venv
	@. .venv/bin/activate