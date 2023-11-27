#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console
print("hello world")

import random

import random

options = ['rock', 'paper', 'scissors']
games_played = 0
games_won = 0

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    while user_choice not in options:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ")
    return user_choice

def get_computer_choice():
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    global games_won
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        games_won += 1
        return "You win!"
    else:
        return "You lose!"

def play_again():
    user_input = input("Do you want to play again? (yes/no): ")
    while user_input not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'.")
        user_input = input("Do you want to play again? (yes/no): ")
    return user_input == 'yes'

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
    games_played += 1
    
    if not play_again():
        print(f"You played {games_played} games and won {games_won} times.")
        break