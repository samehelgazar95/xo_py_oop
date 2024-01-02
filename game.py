#!/usr/bin/env python3
from menu import Menu
from player import Player
from board import Board
import os, sys


class Game:
    def __init__(self):
        self.menu = Menu()
        self.players = [Player(), Player()]
        self.board = Board()
        self.turn = 0


    def start_game(self):
        choice = self.menu.start_msg() 
        if choice == "1":
            self.setup_players()
            os.system('clear')
            self.game_is_running()
        else:
            print("Quit Game, Goodbye!")


    def setup_players(self):
        for (i, player) in enumerate(self.players, start=1):
            print(f"Player {i}.")
            player.enter_name()
            player.enter_symbol()
            print(f">> Name: {player.name} | Symbol: {player.symbol} <<")
            print('-'*20)


    def game_is_running(self):
        self.board.display_board()
        i = 0
        while i < 9:
            try:
                player = self.players[self.turn]
                turn_msg = f"{player.name}'s, Your turn: "
                choice = int(input(turn_msg))

                if 1 <= choice <= 9:
                    if self.board.update_board(player.symbol, choice-1):
                        if self.player_turn():
                            i = i + 1
                            break
                    else:
                        self.clear_then_display("** Choose empty cell **")
                else:
                    self.clear_then_display("** Enter valid num:  1<=num<=9 **")
            except ValueError:
                self.clear_then_display("** Just a num not alpha**")
        self.draw()


    def player_turn(self):
        self.check_win_helper()
        self.turn = 1 - self.turn
        self.clear_then_display()


    def check_win_helper(self):
        if (self.check_win()):
            player = self.players[self.turn]
            self.clear_then_display(f"Winner Winner: {player.name}")
            
            if self.menu.end_msg() == '1':
                self.clear_reset_runGame();
            else:
                self.exit()
                

    def check_win(self):
        winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        for i in winning_positions:
            board = self.board.board
            if board[i[0]] == board[i[1]] == board[i[2]]:
                return True
        return False


    def draw(self):
        print("Draw, No Winner Winner!")
        if self.menu.end_msg() == '1':
                self.clear_reset_runGame()
        else:
            self.exit()

    def clear_then_display(self, message=""):
        os.system('clear')
        self.board.display_board()
        print(message)


    def clear_reset_runGame(self):
        os.system('clear')
        self.board.reset_board()
        self.game_is_running()


    def exit(self):
        print("Quit Game, Goodbye!")
        sys.exit()
        

game = Game()
game.start_game()
