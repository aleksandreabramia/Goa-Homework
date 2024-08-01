#making rock paper scissors
import random

player_choice = input("play rock paper scissors with me choose rock paper or scissors:")
computer_choice =  ["rock", "paper", "scissors"]
computer = (random.choice(computer_choice))

#if player chooses rock

if (player_choice == "rock" and computer == "paper"):
    print("i choose paper you lost")
if(player_choice == "rock" and computer == "scissors"):
    print("i choose scissors you won")
if(player_choice == "rock" and computer == "rock"):
    print("i choose rock its a tie")



if (player_choice == "paper" and computer == "rock"):
    print("i choose rock you won")
if(player_choice == "paper" and computer == "scissors"):
    print("i choose scissors you lost")
if(player_choice == "paper" and computer == "paper"):
    print("i choose paper its a tie")


if (player_choice == "scissors" and computer == "rock"):
    print("i choose rock you lost")
if(player_choice == "scissors" and computer == "paper"):
    print("i choose paper you won")
if(player_choice == "scissors" and computer == "scissors"):
    print("i choose scissors its a tie")