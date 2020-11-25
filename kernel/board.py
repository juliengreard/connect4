#!/usr/bin/env python
# encoding: utf-8

from framework.exceptions import (
    MotorException,
    IllegalMove,
)

class Board(object):

    def __init__(self, w, h):
        self.__width = w
        self.__height = h
        self.__started = False
        self.__board = None

    def start(self):
        self.__started = True
        self.__board = []
        for col in range(self.width):
            self.__board.append([])
    
    def get(self, column, line):
        col = self.__board[column]
        if len(col) <= line:
            return None
        return col[line]
    def play(self, player, column):
        
        if column > len(self.__board):
            raise IllegalMove("Move outside the board !")
        
        col = self.__board[column]
        if len(col) == self.__height:
            raise IllegalMove("This column is full ! {}".format(len(col)))

        col.append(player)

    #######################################

    def display(self):

        def invert_col(col):
            '''
            remplie la colonne d'espaces et 
            la retourne inversée
            '''

            result = []
            for x in col:
                result.append(x)
            while len(result) < self.height:
                result.append(" ")
            result.reverse()
            return result
        
        cols_to_display = []
        for col in self.__board:
            col = invert_col(col)
            cols_to_display.append(col)

        print(" ".join([str(x) for x in range(self.height - 1)])) # print coordinates)

        for line in range(self.height):
            displayed_line = []
            for col in cols_to_display:
                displayed_line.append(col[line])
            print("|".join(displayed_line))

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height
    
    @property
    def board(self):
        return self.__board


        
