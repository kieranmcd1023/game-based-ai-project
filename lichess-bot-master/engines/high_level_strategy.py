#!/usr/bin/env python3

# Imports
import chess
from engine2 import Engine2
from mid_winning import MidWinning

# Pieces: Pawns, Knights, Bishops, Rooks, Queens
PIECE_VALUES = {1:1, 2:3, 3:3, 4:5, 5:9}
DEFAULT_POINTS = 39

# States (sub-engines):
#	- Opening State (book openings)
#	- Midgame-Winning State
#	- Midgame-Not-Winning State
#	- Endgame State (few pieces, look for checkmates)
# 	- Killshot State (aggressively pursue ending the game, winning or tying)

class ControlMechanism:
	def __init__(self):
		#self.color = color
		self.state = 1
		self.state_0 = Engine2() # irrelevant - remove later but keep for now
		self.state_1 = MidWinning()
		self.state_2 = Engine2()
		self.state_3 = Engine2()
		self.state_4 = Engine2()
		self.engine_array = [self.state_0, self.state_1, self.state_2, self.state_3, self.state_4]

	def score_board(self, board, color):
		score = 0
		for key in PIECE_VALUES:
			score += PIECE_VALUES[key] * len(list(board.pieces(key, color)))
		return score

	#def opening_state(self, board):
		# Transitions out:
		# 	- Go to one of the midgame states if number of moves > 4
		# 	- [Future]: transition out when book openings exhausted
	#	if board.fullmove_number > 4:
	#		if self.score_board(board, self.color) > self.score_board(board, not self.color):
	#			self.state = 1
	#		else:
	#			self.state = 2

	def midgame_winning_state(self, board):
		# Transitions out:
		# 	- Go to killshot state if a player has twice as many points as the other (or more)
		# 	- Go to endgame state if either player has fewer than 13 points left
		# 	- Go to midgame-not-winning state if tied or losing in points
		our_points = self.score_board(board, board.turn) #self.color)
		opp_points = self.score_board(board, not board.turn) #self.color)
		if our_points >= 2 * opp_points or opp_points >= 2 * our_points:
			self.state = 4
		elif our_points < 13 or opp_points < 13:
			self.state = 3
		elif our_points <= opp_points:
			self.state = 2

	def midgame_not_winning_state(self, board):
		# Transitions out:
		# 	- Go to killshot state if a player has twice as many points as the other (or more)
		# 	- Go to endgame state if either player has fewer than 13 points left
		# 	- Go to midgame-winning state if winning in points
		our_points = self.score_board(board, board.turn) #self.color)
		opp_points = self.score_board(board, not board.turn) #self.color)
		if our_points >= 2 * opp_points or opp_points >= 2 * our_points:
			self.state = 4
		elif our_points < 13 or opp_points < 13:
			self.state = 3
		elif our_points > opp_points:
			self.state = 1

	def endgame_state(self, board):
		# Transitions out:
		# 	- Go to killshot state if a player has twice as many poins as the other (or more)
		our_points = self.score_board(board, board.turn) #self.color)
		opp_points = self.score_board(board, not board.turn) #self.color)
		if our_points >= 2 * opp_points or opp_points >= 2 * our_points:
			self.state = 4

	def killshot_state(self, board):
		# Transitions out:
		# 	- Go to endgame state if neither player has twice as many points as the other (or more), and either player has fewer than 13 points
		#	- Go to midgame-winning state if neither player has twice as many points as the other (or more), and we have more points
		# 	- Go to midgame-not-winning state if neither player has twice as many points as the other (or more), and we have fewer points (or the same amount)
		our_points = self.score_board(board, board.turn) #self.color)
		opp_points = self.score_board(board, not board.turn) #self.color)
		if our_points < 2 * opp_points and opp_points < 2 * our_points:
			if our_points < 13 or opp_points < 13:
				self.state = 4
			elif our_points > opp_points:
				self.state = 1
			else:
				self.state = 2

	def make_move(self, board):
		# Make the move
		self.engine_array[self.state].make_move(board)

		# Transition into new state, or stay the same
		#if self.state == 0:
		#	self.opening_state(board)
		if self.state == 1:
			self.midgame_winning_state(board)
		elif self.state == 2:
			self.midgame_not_winning_state(board)
		elif self.state == 3:
			self.endgame_state(board)
		elif self.state == 4:
			self.killshot_state(board)

