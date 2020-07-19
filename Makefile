install:
	pip3 install -r requirements.txt

run:
	clear
	python3 src/snake/main.py

profile:
	clear
	python3 -m cProfile -s ncalls src/snake/main.py