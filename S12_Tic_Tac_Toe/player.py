from move import Move
import random
from board import Board # Import Board to use Board.EMPTY_CELL

class Player:
    PLAYER_MARKER = "X"
    COMPUTER_MARKER = "O"
 
    def __init__(self, is_human=True):
        self._is_human = is_human
 
        if is_human:
            self._marker = Player.PLAYER_MARKER
        else:
            self._marker = Player.COMPUTER_MARKER
 
    @property
    def is_human(self):
        return self._is_human
 
    @property
    def marker(self):
        return self._marker
 
    def get_move(self):
        if self._is_human:
            return self.get_human_move()
        else:
            return self.get_computer_move()
            # Para o design atual, vamos passar o board em ticTacToeGame.py

    def get_human_move(self):
        while True:
            try:
                user_input = int(input(f"Player {self._marker}, please enter your move (1-9): "))
                move = Move(user_input)
                if move.is_valid():
                    break
                else:
                    print("Invalid input. Please enter an integer between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        return move
 
    def get_computer_move(self, board_instance): # Aceita a instância do tabuleiro
        available_moves = []
        for r_idx, row in enumerate(board_instance.game_board):
            for c_idx, cell in enumerate(row):
                if cell == Board.EMPTY_CELL:
                    available_moves.append(r_idx * 3 + c_idx + 1)
        
        if not available_moves: # Não deve acontecer se check_is_tie for chamado antes
            return None

        chosen_value = random.choice(available_moves)
        move = Move(chosen_value)
        print(f"Computer ({self.marker}) chose move: {move.value}")
        return move