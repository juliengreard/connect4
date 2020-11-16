#!/usr/bin/env python
# encoding: utf-8

from players.base_player import BasePlayer

class ManualPlayer(BasePlayer):

    def __init__(self, name):
        super(ManualPlayer, self).__init__(name = name)

    def play(self, board):
        col = input("[ {} ] On which column do you play ?\n".format(self.name))
        col = int(col)
        return col
