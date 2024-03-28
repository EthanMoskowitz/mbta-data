init:
	pip install -q -r requirements.txt

run: init
	python main.py

tests: init
	pytest test

clean:
	find $(CURDIR) -type d -name "__pycache__" -exec rm -r {} +
	find $(CURDIR) -type d -name ".pytest_cache" -exec rm -r {} +