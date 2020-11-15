#!/usr/bin/env python
# encoding: utf-8

import random

class BasePlayer(object):

    def __init__(self, name):
        self.name = name
        self.disqualified = False
    
    def play_random(self, board):
        choices = []
        for colNb in range(board.width):
            if len(board.board[colNb]) < board.height:
                choices.append(colNb)
        return random.choice(choices)