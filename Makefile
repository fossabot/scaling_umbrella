all: test

install:
	pip install -r requirements.txt

test: install
	coverage run -m pytest
	coverage report
	coverage xml

run: install
	python main.py fixtures/coverage_1.xml fixtures/coverage_2.xml