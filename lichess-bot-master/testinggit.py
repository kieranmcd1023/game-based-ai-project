#!/usr/bin/env python3

import chess
import chess.uci

if __name__ == '__main__':
	#engine = chess.uci.popen_engine('engines/random_engine.py')
	#engine = chess.uci.popen_engine('engines/stockfish-11-64')
	#engine = chess.uci.popen_engine('engines/sunfish.py')
	engine = chess.uci.popen_engine('engines/uci_engine.py')
	#engine.debug(True)
	#print(engine.is_alive())
	#print(engine.get_the_info())
	print('before uci()')
	engine.uci()
	print('after uci()')
	#engine.ucinewgame()
	engine.go()
	print('after go()')
#	print('enter loop')
#	while True:
#		engine.go(movetime=1000)
#		print('looping')

	engine.kill()
