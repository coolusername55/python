import os
from time import sleep 
import random

def Login():
  Username = input("Please enter a username ")
  Age = input("Please enter your age: ")

  print("Welcome " + Username + ". Please wait while the game loads.")

  sleep(2)
  os.system('clear')
  MainMenu()

def MainMenu():
  print("Welcome to the number guessing game!")
  
  print("\nPlease choose one of the following options: ")
  MenuChoice = int(input("1) Play Game \n2) Exit "))

  if(MenuChoice ==1):
    Game()

  else:
   Exit()


def Game():
  os.system('clear')
  print("I am thinking of a random number between 1 and 25.")
  print("Can you guess what it is?")

  RandomNumber = random.randint(1,25)

  while True:
    UserGuess = int(input("What is your guess?: "))
    if(UserGuess != RandomNumber):
      print("Incorrect guess. You suck! guess again chicken.")
      sleep(1)
      os.system('clear')
    else:
      print("Correct. Congratulations son you did it you is number one!!")
    

      ReturnMenu = int(input("Would you like to return to the main menu? \n1) Yes\n2) No "))

      if(ReturnMenu ==1):
        os.system('clear')
        MainMenu()
      else:
        Exit()


def Exit():
  print("Thank you for playing")
  sleep(1)
  os._exit(0)

  
Login()