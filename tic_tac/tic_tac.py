from flask import Flask, render_template, request, session, redirect
from .models import Game
from .models import Board
from .models import Player

app = Flask(__name__) 
app.config.from_object(__name__)
app.config.from_envvar('TIC_TAC_SETTINGS', silent=True)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_game')
def new_game():
    global game
    game = Game()
    current_player = game.current_player
    board = game.board

    return render_template('game.html', current_player = current_player, board = board)

@app.route('/move/<x>/<y>/<z>/<a>')
def move(x, y, z, a):
    coordinates = {'x': int(x), 'y': int(y), 'z': int(z), 'a': int(a)}

    game.board.mark_square(game.current_player.symbol, coordinates)
    if game.current_player.is_winner_on_small_board(game.board, coordinates):
        game.board.mark_small_board(coordinates, game.current_player.symbol)
        game.board.mark_main_board(coordinates, game.current_player.symbol)
        game.board.remove_small_board_from_available(coordinates)

        if game.current_player.is_winner(game.board):
            return render_template('win.html', winner = game.current_player, board = game.board)
                
    game.board.small_board_for_next_turn(coordinates)
    game.change_player()

    return render_template('game.html', current_player = game.current_player, board = game.board)    