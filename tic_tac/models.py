import random

class Game:
    def __init__(self):
        self.board = Board()
        self.player1 = Player("O")
        self.player2 = Player("X")
        self.current_player = random.choice([self.player1, self.player2])

    def change_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

class Board:
    def __init__(self):
        self.squares = self.initialize_board()
        self.main_board = [['', '', ''], ['', '', ''], ['', '', '']]
        self.available_small_boards = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        self.current_small_board = []

    def initialize_board(self):
        squares = [[[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']]],[[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']]],[[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']],[['', '', ''],['', '', ''],['', '', '']]]]
        return squares

    def is_move_possible(self, coordinates):
        if self.is_square_empty(coordinates):
            if self.current_small_board:
                if self.is_move_on_proper_small_board(coordinates):
                    return True
                else:
                    return False            
            return True
        else:
            return False

    def is_square_clickable(self, coordinates):
        if self.is_square_empty(coordinates):
            if self.current_small_board == []:
                return True
            else:
                if self.is_on_proper_small_board(coordinates):
                    return True
                else:
                    return False    

        else:
            return False

    def mark_square(self, symbol, coordinates):
        self.squares[coordinates['x']][coordinates['y']][coordinates['z']][coordinates['a']] = symbol

    def small_board_for_next_turn(self, coordinates):
        if [coordinates['z'], coordinates['a']] in self.available_small_boards:
            self.current_small_board = { 'x': coordinates['z'], 'y': coordinates['a'] }
        else:
            self.current_small_board = []

    def mark_small_board(self, coordinates, symbol):
        for x in [0, 1, 2]:
            for y in [0, 1, 2]:  
                self.squares[coordinates['x']][coordinates['y']][x][y] = symbol

    def mark_main_board(self, coordinates, symbol):
        self.main_board[coordinates['x']][coordinates['y']] = symbol

    def check_rows_for_win(self, symbol, coordinates = {}):
        if not  coordinates:
            for x in range(3):
                if self.main_board[x][0] == self.main_board[x][1] == self.main_board[x][2] == symbol:
                    return True

            return False
        else: 
            for x in range(3):
                if self.squares[coordinates['x']][coordinates['y']][x][0] == self.squares[coordinates['x']][coordinates['y']][x][1] == self.squares[coordinates['x']][coordinates['y']][x][2] == symbol:
                    return True

            return False

    def check_columns_for_win(self, symbol, coordinates = {}):
        if not  coordinates:
            for x in range(3):
                if self.main_board[0][x] == self.main_board[1][x] == self.main_board[2][x] == symbol:
                    return True
            return False
        else:
            for x in range(3):
                if self.squares[coordinates['x']][coordinates['y']][0][x] == self.squares[coordinates['x']][coordinates['y']][1][x] == self.squares[coordinates['x']][coordinates['y']][2][x] == symbol:
                    return True

            return False
    
    def check_diagonals_for_win(self, symbol, coordinates = {}):
        if not  coordinates:
            if self.main_board[0][0] == self.main_board[1][1] == self.main_board[2][2] == symbol or self.main_board[2][0] == self.main_board[1][1] == self.main_board[0][2] == symbol:
                return True
            else:
                return False
        else:
            if self.squares[coordinates['x']][coordinates['y']][0][0] == self.squares[coordinates['x']][coordinates['y']][1][1] == self.squares[coordinates['x']][coordinates['y']][2][2] == symbol or self.squares[coordinates['x']][coordinates['y']][2][0] == self.squares[coordinates['x']][coordinates['y']][1][1] == self.squares[coordinates['x']][coordinates['y']][0][2] == symbol:
                return True
            else:
                return False      

    def set_small_board_winner(self, player, coordinates):
        self.squares[coordinates[x]][coordinates[y]] = player.symbol #[[player.symbol()]*3]*3

    def remove_small_board_from_available(self, coordinates):
        self.available_small_boards.remove([coordinates['x'], coordinates['y']])

    def is_on_proper_small_board(self, coordinates):
        if self.current_small_board != []:
            if self.current_small_board['x'] == coordinates['x'] and self.current_small_board['y'] == coordinates['y']:
                return True
            else:
                return False

    def is_square_empty(self, coordinates):
        if self.squares[coordinates['x']][coordinates['y']][coordinates['z']][coordinates['a']] == '':
            return True
        else:
            return False


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def place_mark(self, board, coordinates):
        if board.is_move_possible == True:
            board.mark_square(self.symbol)
            return True
        else:
            return False

    def is_winner_on_small_board(self, board, coordinates):
        if board.check_rows_for_win(self.symbol, coordinates) or board.check_columns_for_win(self.symbol, coordinates) or board.check_diagonals_for_win(self.symbol, coordinates):
            return True
        else: 
            return False


    def is_winner(self, board):

        if board.check_rows_for_win(self.symbol) or board.check_columns_for_win(self.symbol) or board.check_diagonals_for_win(self.symbol):
            self.is_winner = True
            return True
        else:
            return False

    def symbol(self):
        return self.symbol