#!/usr/bin/env python3


class Player:
    def __init__(self):
        self.name = "";
        self.symbol = "";
        
    def enter_name(self):
        name = input("Enter name: ")
        self.name = name
    
    def enter_symbol(self):
        while True:
            symbol = input(f"{self.name}, enter symbol: ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("!!Symbol must be one alpha!!")

