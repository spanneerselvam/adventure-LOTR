import random
import time

def displayIntro():
  print("After a long journey from Mordor, after defeating orks and goblins, after meeting the elves and battling the spider, Shelob, it is time to finally come home to the shire.")
  time.sleep(3)
  print("You come to the crossroads of your trip; however, only one path takes you back to the rolling green hills of the shire.")
  print("And the other paths?")
  time.sleep(3)
  print("They will lead you to danger...")

def choosenPath():
  path = ""
  while path != 1 and path != 2:
    path = input("Which path will you choose? Enter '1' for East or '2' for West: ")
    return path
def checkPath(choosenPath):
  print("You head down the path...")
  time.sleep(2)
  print("You see a pub that looks familiar... That must be a good sign!")
  time.sleep(2)
  print("But then, your stomach does a backwards flip...")
  print()
  time.sleep(4)

  correctPath= random.randint(1,2)

  if choosenPath == str(correctPath):
    print("You were right! It is Prancing Pony where your buddy Frodo caused quite a stir!")
    print("Welcome home, little Shireling!")
  else:
    print()
    print("Ahh! The pub is a watering hole for a bunch of urukai!")
    time.sleep(2)
    print("You pull out your sword, ready to fight.")
    time.sleep(4)
    print()
    print("However, it's too late... You're being taken as a prisoner and thus erasing your existence here on Middle Earth.")
    quit()

playAgain = "yes"

while playAgain == "yes" or playAgain == "y":
  displayIntro()
  choice = choosenPath()
  checkPath(choice)
  playAgain = input("Do you want to play again? Enter 'yes' or 'y' to play again.")

  
