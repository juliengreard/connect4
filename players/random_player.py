#!/usr/bin/env python
# encoding: utf-8

from players.base_player import BasePlayer

class RandomPlayer(BasePlayer):

    def __init__(self, name):
        super(RandomPlayer, self).__init__(name = name)

    def play(self, board):
        return self.play_random(board)
            
