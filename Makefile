init:
	pip3 install -r requirements.txt --break-system-packages

run:
	python3 main/main.py

tests:
	pytest test