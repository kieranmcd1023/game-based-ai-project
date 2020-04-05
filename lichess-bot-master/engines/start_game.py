#!/usr/bin/env python3

import chess
import requests

if __name__ == '__main__':
	url = 'https://lichess.org/api/challenge/TrolliumBot'
	my_obj = {'rated': False, 'clock.limit': 300, 'clock.increment': 8}
	x = requests.post(url, data = my_obj)
	print(x.text)
