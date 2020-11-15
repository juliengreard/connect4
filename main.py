#!/usr/bin/env python
# encoding: utf-8

from kernel.board import Board
from kernel.config import (
    NbAlignToWin,
    NbOfPlayer,
    Columns,
    Lines,
    Player1,
    Player2,
)
from framework.exceptions import (
    IllegalMove,
    MotorException,
)
from players import (
    ManualPlayer,
    RandomPlayer,
)
from kernel.mods import Players

def start():
    board = Board(Columns, Lines)
    board.start()
    return board


def create_player(player_type):

    player = None
    if player_type == Players.Manual:
        name = raw_input("What's your name ? \n")
        print "player added : {}".format(name)
        player = ManualPlayer(name)
    elif player_type == Players.Bot:
        player = RandomPlayer("RandomBot")
    else:
        raise MotorException("No other player type is available!")

    return player

def game_setup():

    p1 = create_player(Player1)
    p2 = create_player(Player2)

    return [p1, p2, ]

def has_player_won(board):
    winner = None

    # méthode pas opti : on cherche
    # pour chaque emplacement s'il
    # est le 1er élément d'une suite

    def line_possible(lin, col, board):
        return col + 3 < board.width
    
    def diagdown_possible(lin, col, board):
        return lin > 3 and line_possible(lin, col, board)
        
    def diagup_possible(lin, col, board):
        return column_possible(lin, col, board) and line_possible(lin, col, board)
    
    def column_possible(lin, col, board):
        return line + 3 < board.height
    
    for line in range(board.height):
        for col in range(board.width):

            if board.get(col,line):
                pawn = board.get(col,line)
                line_win = False
                diag_win = False
                column_win = False
                # TODO, prendre en compte la variable NbAlignToWin
                if line_possible(line, col, board):
                    line_win = (pawn == board.get(col + 1,line) and  pawn == board.get(col + 2 ,line) and  pawn == board.get(col + 3,line))
                if diagup_possible(line, col, board):
                    diag_win = (pawn == board.get(col + 1, line + 1) and  pawn == board.get(col + 2, line + 2 ) and  pawn == board.get(col + 3,line + 3))
                if diagdown_possible(line, col, board):
                    diag_win = (pawn == board.get(col - 1, line - 1) and  pawn == board.get(col - 2, line - 2) and  pawn == board.get(col - 3,line - 3))
                if column_possible(line, col, board):
                    column_win = (pawn == board.get(col, line + 1 ) and  pawn == board.get(col, line + 2) and  pawn == board.get(col, line + 3))
                
                if line_win or diag_win or column_win:
                    return True, pawn

    return False, winner

def is_board_full(board):
    
    for col in board.board:
        if len(col) != board.height:
            return False
    return True

def get_remaining_players(players):
    return [x for x in players if x.disqualified == False]


def is_game_over(board, players):
    
    winner = None
    game_over, winner = has_player_won(board)

    remaining_players = get_remaining_players(players)
    if len(remaining_players) == 0:
        return True, None
    elif len(remaining_players) == 1:
        return True, remaining_players[0]
    if game_over:
        return True, winner
    if is_board_full(board):
        return True, winner
    return False, None 
    
game_over = False
board = start()
players = game_setup()
signs = ["X", "0"]
players_marks = {}
for player in range(len(players)):
    players_marks[players[player].name] = signs[player]

for k, v in  players_marks.iteritems():
    print "Player : {} plays with {}".format(k, v)
winner = None

while (not game_over):

    for player in players:
        try:
            move = player.play(board)
            board.play(players_marks[player.name], move)
        except IllegalMove as e:
            print e.message
            print "Player : {} is disqualified".format(player.name)
            player.disqualified = True
        finally:
            game_over, winner = is_game_over(board, players)
            winner_name = None
            for k, v in  players_marks.iteritems():
                if winner == v:
                   winner = k
            board.display()
            if game_over:
                break

if winner:
    print "Game over, player {} won".format(winner)
else:
    print "Game over, draw"

