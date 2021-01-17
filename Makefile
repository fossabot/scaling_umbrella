all: run

install:
	pip install -r requirements.txt

test: install
	coverage run -m pytest
	coverage report
	coverage xml