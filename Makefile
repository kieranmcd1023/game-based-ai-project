
install:
	pip3 install python-chess==0.24.1
	pip install python-chess==0.24.1
	pip3 install backoff
	pip install backoff

test:
	cd lichess-bot-master && python3 lichess-bot.py -u


clean:
	

build:
	pip3 install python-chess==0.24.1
	pip install python-chess==0.24.1
	pip3 install backoff
	pip install backoff
