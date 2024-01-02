#!/usr/bin/env python3


class Menu:
    def start_msg(self):
        print("Hello XO:")
        choice = input("Play (1), Quit Game (else): ")
        print('-'*20)
        return choice
    
    def end_msg(self):
        return input("Restart (1), Quit Game (else): ")
