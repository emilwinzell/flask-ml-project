install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=cli --cov=app --cov=utilscli --cov=app test_app.py

format:
	black *.py

deploy:
	# todo
	
all: install lint test format deploy