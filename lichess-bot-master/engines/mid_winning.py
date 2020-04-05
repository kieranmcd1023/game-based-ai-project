#!/usr/bin/env python3
# Engine 3 - Simple Search Algorithm (Mid-Game, Winning)

# This engine makes moves by looking several moves into the future, and
# uses MinMax to choose the best (board scoring is based on piece value)

import chess
import random

# Pieces: Pawns, Knights, Bishops, Rooks, Queens
PIECE_VALUES = {1:1, 2:3, 3:3, 4:5, 5:9}
DEFAULT_POINTS = 39

class MidWinning:
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

	def best_variance(self, options, board):
		# Trades are good here - the less cluttered the board, the better
		least_cluttered_board_moves = [options[0]]
		least_cluttered_board_score = -1
		for move in options[1:]:
			total_piece_score = 0
			for key in PIECE_VALUES:
				total_piece_score += PIECE_VALUES[key] * len(list(board.pieces(key, True)))
				total_piece_score += PIECE_VALUES[key] * len(list(board.pieces(key, False)))
			if total_piece_score == least_cluttered_board_score:
				least_cluttered_board_moves.append(move)
			elif total_piece_score > least_cluttered_board_score:
				least_cluttered_board_moves = []
				least_cluttered_board_moves.append(move)
				least_cluttered_board_score = total_piece_score
		return least_cluttered_board_moves

	def broken_best_variance(self, options, board):
		variance_score = -1000000
		mid_winning_options = []
		for move in options:
			temp_board = board.copy()
			temp_board.push(move)
			user_variance = self.score_board(temp_board, temp_board.turn)
			opponent_best_move = self.max_move(temp_board)
			temp_board_next = temp_board.copy()
			temp_board_next.push(opponent_best_move)
			opponent_variance = self.score_board(temp_board_next, temp_board_next.turn)
			if (user_variance + opponent_variance) == variance_score:
				mid_winning_options.append(move)
			elif (user_variance + opponent_variance) > variance_score:
				variance_score = user_variance + opponent_variance
				mid_winning_options = []
				mid_winning_options.append(move)
		return mid_winning_options



	def make_move(self, board):
		#board.push(self.max_move(board))
		opponent_worst_best_score = -1000000
		opponent_worst_best_options = []
		for move in list(board.legal_moves):
			temp_board_0 = board.copy()
			temp_board_0.push(move)
			if temp_board_0.is_game_over(): # choose this if it's a win/draw
				opponent_worst_best_options = []
				opponent_worst_best_options.append(move)
				break
			# Get opponent's 'best' move
			opponent_best_move = self.max_move(temp_board_0)
			temp_board_1 = temp_board_0.copy()
			temp_board_1.push(opponent_best_move)
			opponent_best_move_score = self.score_board(temp_board_1, temp_board_1.turn)
			if opponent_best_move_score == opponent_worst_best_score:
				opponent_worst_best_options.append(move)
			elif opponent_best_move_score > opponent_worst_best_score:
				opponent_worst_best_score = opponent_best_move_score
				opponent_worst_best_options = []
				opponent_worst_best_options.append(move)
		if len(opponent_worst_best_options) > 1:
			#print(opponent_worst_best_options)
			opponent_worst_best_options = self.best_variance(opponent_worst_best_options, board)
		board.push(random.choice(opponent_worst_best_options))

if __name__ == '__main__':
	e0 = MidWinning()
	the_board = chess.Board()
	counter = 0
	while not the_board.is_game_over():
		if the_board.turn:
			print('WHITE TURN')
		else:
			print('BLACK TURN')
		print(the_board.unicode())
		print('')
		e0.make_move(the_board)
	print('--Final Board--')
	print(the_board.unicode())
	print('Result: ',the_board.result())
	print('Full moves: ', the_board.fullmove_number)

