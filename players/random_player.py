#!/usr/bin/env python
# encoding: utf-8

import random

from players.base_player import BasePlayer

class RandomPlayer(BasePlayer):

    def __init__(self, name):
        super(RandomPlayer, self).__init__(name = name)

    def play(self, board):
        choices = []
        for colNb in range(board.width):
            if len(board.board[colNb]) < board.height:
                choices.append(colNb)
        return random.choice(choices)
            
