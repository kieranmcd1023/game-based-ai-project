#!/usr/bin/env python3
# Opening Engine - use book moves until done

import chess
import chess.polyglot
import random

class OpeningEngine:
	def __init__(self):
		self.reader = chess.polyglot.open_reader("gm2001.bin")
		self.done = False

	def make_move(self, board):
		try:
			next_move = self.reader.weighted_choice(board).move
			print(next_move)
			board.push(next_move)
		except:
			self.done = True

if __name__ == '__main__':
	board = chess.Board()
	oe = OpeningEngine()
	while (not oe.done):
		print(board.unicode())
		oe.make_move(board)
	#with chess.polyglot.open_reader("gm2001.bin") as reader:
	#	for entry in oe.reader.find_all(board):
	#		print(entry.move, entry.weight, entry.learn)
