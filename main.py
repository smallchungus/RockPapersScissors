
"""
User inputs rock paper or scissors  and plays against the computer.
The computer randomly selects rock papers and scissors every throw
if I throw rock, paper beats rock and rock beats scissors and 2 rocks are a tie
if I throw paper, scissors beats paper, and paper beats rock and 2 papers are a tie.
if I throw scissors, rock beats scissors, scissors beats paper, and 2 scissors are a tie.

"""

import random

def fun1():

    userthrow = input("Rock Paper or Scissors: ").lower()
    computer = random.choice(["rock", "paper", "scissors"])
    didyouwin(userthrow, computer)


def didyouwin (userthrow, computerthrow):

    if ( userthrow == "rock" and computerthrow == "paper" ) or ( userthrow == "scissors" and computerthrow == "rock") \
    or ( userthrow == "paper" and computerthrow == "scissors" ):
        print (f"You threw {userthrow} and the computer threw {computerthrow} so you lost")

    if ( userthrow == "rock" and computerthrow == "scissors" ) or ( userthrow == "scissors" and computerthrow == "paper") \
    or ( userthrow == "paper" and computerthrow =="rock"):
        print(f"You threw {userthrow} and the computer threw {computerthrow} so you won")

    if ( userthrow == computerthrow):
        print(f"You threw {userthrow} and the computer threw {computerthrow} so it's a tie")


fun1()