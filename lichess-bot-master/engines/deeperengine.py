#!/usr/bin/env python3
# Deeper Engine

# This engine makes moves by looking several moves into the future, and
# uses MinMax to choose the best (board scoring is based on piece value)

import chess
import random
from engine2 import Engine2

# Pieces: Pawns, Knights, Bishops, Rooks, Queens
PIECE_VALUES = {1:1, 2:3, 3:3, 4:5, 5:9}
DEFAULT_POINTS = 39
DEPTH = 3

class DeeperEngine:
	def __init__(self):
		pass
	def score_board(self, board, color):
		opponent_score = 0
		user_score = 0
		for key in PIECE_VALUES:
			opponent_score += PIECE_VALUES[key] * len(list(board.pieces(key, color)))
			user_score += PIECE_VALUES[key] * len(list(board.pieces(key, not color)))
		return opponent_score - user_score
	def max_move(self, board): # give the 'best' move based on score
		best_score = DEFAULT_POINTS
		best_options = []
		for move in list(board.legal_moves):
			temp_board = board.copy()
			temp_board.push(move)
			temp_score = self.score_board(temp_board, temp_board.turn)
			if temp_score == best_score:
				best_options.append(move)
			elif temp_score < best_score:
				best_score = temp_score
				best_options = []
				best_options.append(move) # reset list and add the new move
		return random.choice(best_options)

	def make_move(self, board):
		best_move = self.make_move_recursive(board, DEPTH, board.turn)[0]
		board.push(best_move)
		#opponent_worst_best_score = -1000000
		#opponent_worst_best_options = []
		#for move in list(board.legal_moves):
		#	temp_board_0 = board.copy()
		#	temp_board_0.push(move)
		#	if temp_board_0.is_game_over(): # choose this if it's a win/draw
		#		opponent_worst_best_options = []
		#		opponent_worst_best_options.append(move)
		#		break
		#	# Get opponent's 'best' move
		#	opponent_best_move = self.max_move(temp_board_0)
		#	temp_board_1 = temp_board_0.copy()
		#	temp_board_1.push(opponent_best_move)
		#	opponent_best_move_score = self.score_board(temp_board_1, temp_board_1.turn)
		#	if opponent_best_move_score == opponent_worst_best_score:
		#		opponent_worst_best_options.append(move)
		#	elif opponent_best_move_score > opponent_worst_best_score:
		#		opponent_worst_best_score = opponent_best_move_score
		#		opponent_worst_best_options = []
		#		opponent_worst_best_options.append(move)
		#board.push(random.choice(opponent_worst_best_options))

	def make_move_recursive(self, board, how_deep, original_color):
		if how_deep == 1:
			multiplier = -1 if original_color == board.turn else 1
			best_move = self.max_move(board)
			temp_board = board.copy()
			temp_board.push(best_move)
			if temp_board.is_game_over():
				#print('our bot sees a checkmate (base)')
				#print(temp_board.unicode())
				return [best_move, -1000*multiplier]
			best_score = self.score_board(temp_board, original_color)
			return [best_move, best_score]


		it_is_our_turn = True if original_color == board.turn else False
		best_score = -1000000 if it_is_our_turn else 1000000
		best_moves = []
		for move in list(board.legal_moves):
			temp_board_0 = board.copy()
			temp_board_0.push(move)
			if temp_board_0.is_game_over():
				#print('our bot sees a checkmate')
				#print('depth: ' + str(how_deep))
				multiplier = 1 if original_color == board.turn else -1
				return [move, 1000*multiplier]
			# Recursive call
			best_of_batch = self.make_move_recursive(temp_board_0, how_deep - 1, original_color)
			if best_of_batch[1] == best_score:
				best_moves.append(move)
			if it_is_our_turn:
				if best_of_batch[1] > best_score:
					best_score = best_of_batch[1]
					best_moves = []
					best_moves.append(move)
			else:
				if best_of_batch[1] < best_score:
					best_score = best_of_batch[1]
					best_moves = []
					best_moves.append(move)
		return [random.choice(best_moves), best_score]



if __name__ == '__main__':
	e0 = DeeperEngine()
	e2 = Engine2()
	the_board = chess.Board()
	counter = 0
	while not the_board.is_game_over():
		if the_board.turn:
			print('WHITE TURN')
			e0.make_move(the_board)
		else:
			print('BLACK TURN')
			e2.make_move(the_board)
		print(the_board.unicode())
		print('')
#		e0.make_move(the_board)
	print('--Final Board--')
	print(the_board.unicode())
	print('Result: ',the_board.result())
	print('Full moves: ', the_board.fullmove_number)

