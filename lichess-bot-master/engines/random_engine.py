#!/usr/bin/env python3

import chess
import random

#def position():
#	print('position')
#def setoption():
#	print('setoption')
#def go():
#	print('go')
#def bench():
#	print('bench')

def get_the_info():
	print('abc123')

class ChessEngine():
	def __init__(self):
		print('initializing...')
	def get_the_info(self):
		print('blah blah')
	def pick_move(self, Board):
		print('pick_move')
		raise NotImplementedError("needs to be implemented")
		#pass
		#return random.choice(list(Board.legal_moves))
	def start_new_game(self):
		print('start_new_game')
	def ready_engine(self):
		print('ready_engine')
	def release_resources(self):
		print('release_resources')

if __name__ == '__main__':
	print('in main...')
