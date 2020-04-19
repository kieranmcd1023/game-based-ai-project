#!/usr/bin/env python3
# Monte Carlo Engine

import chess
import random

class MonteCarloEngine:
	def __init__(self):
		self.max_sims = 10000

	def finish_game(self, board, player_is_white):
		while not board.is_game_over:
			board.push(random.choice(list(board.legal_moves)))
		result = board.result()
		if result == '1/2-1/2':
			return 0.5
		elif result == '1-0' and player_is_white == True:
			return 1
		elif result == '0-1' and player_is_white == False:
			return 1
		return 0

	def make_move(self, board):
		all_moves = list(board.legal_moves)
		all_scores = [0 for move in all_moves]
		for i in range(self.max_sims):
			index = i % len(all_moves)
			chosen_move = all_moves[index]
			temp_board = board.copy()
			temp_board.push(chosen_move)
			all_scores[index] += self.finish_game(temp_board, board.turn)
		best_move = all_moves[0]
		best_score = all_scores[0]
		for i in range(1, len(all_moves)):
			if all_scores[i] > best_score:
				best_score = all_scores[i]
				best_move = all_moves[i]
		board.push(best_move)

