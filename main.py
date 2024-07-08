from sys import exit
from player import Player
from world import Map, Empty_Room, Enemy_Room, Treasure_Room, Puzzle_Room, Portal_Inside_Portal_Room, Start_Room, Stop_Room
from random import randint, choice
from time import sleep
from items import *
from colorama import Fore

Blue = Fore.BLUE
Green = Fore.GREEN
Yellow = Fore.YELLOW
Red = Fore.RED
Magenta = Fore.MAGENTA
Black = Fore.BLACK
White = Fore.WHITE
Cyan = Fore.CYAN

map = Map()

def setup():
  
  weapons = [Sword(), Dagger(), Kitchen_Knife(), Bow(), Spiked_Arrow_Bow(), Baseball_Bat(), Spiked_Baseball_Bat(), BB_Gun()]
  print("Hello!")
  name = input(Yellow + "\nName?: " + White)
  P1 = Player(name, choice(weapons))
  
  return P1

def transistion(P1, win, croom):

    if win == True:
      P1.x += 1
      croom = map[P1.x]
      

      
    elif win == False:
      if type(map[P1.x - 1]) == Start_Room or type(map[P1.x-2]) == Start_Room:
        P1.x += 0
        
      else:
        P1.x += randint(-2, 4)
        croom = map[P1.x]

    print("".center(50, '~'))
    if P1.HP <= 0:
      game_over()
    else:
      print("\nYour Current Stats:")
      print(f"\n  Name: {P1.name}\n  Weapon: {P1.weapon}\n ", Cyan + "HP:", White + f"{P1.HP}")
      input("\nPress Enter To Continue: ")
      print("".center(50, '-'))
      print("\nYou Fall Out Of The Portal\n")
      sleep(2)
      
    if type(croom) == Empty_Room:
      room = Empty_Room()
      room.empty()

    elif type(croom) == Enemy_Room:
      room=Enemy_Room()
      room.battle(P1)

    elif type(croom) == Treasure_Room:
      room=Treasure_Room()
      room.treasure(P1)

    elif type(croom) == Puzzle_Room:
      num = randint(1, 3)
      if num == 1:
        room=Puzzle_Room()
        room.puzzle_random_puzzle1(P1)

      elif num == 2:
        room=Puzzle_Room()
        room.puzzle_random_puzzle2(P1)

      elif num == 3:
        room=Puzzle_Room()
        room.puzzle_random_puzzle3(P1)

    elif type(croom) == Portal_Inside_Portal_Room:
      room=Portal_Inside_Portal_Room()
      room.portal_inside_portal()

    elif type(croom) == Stop_Room:
      game_finish()
    return croom


def game_over():
  print("\nYou Run Out Of Health...")
  sleep(2)
  print("\n\n\nGame Over!")
  exit()
  
def game_finish():
  print("\nYou Come Out Of The Portal...")
  sleep(0.7)
  print("\nYou See Light...")
  sleep(0.7)
  print("\nYou See People...")
  sleep(0.7)
  print("\nYou See Houses...")
  sleep(0.7)
  print("\nYour...")
  sleep(0.7)
  print("\nHome...")
  sleep(0.7)
  print("\n\n\n\nYou Won!\nThanks For Playing!")
  input("\nPress Enter To Exit:")
  exit()
  
def main():
  
  P1 = setup()
  croom = map[P1.x]
  win = True
  while P1.HP > 0:
    croom = transistion(P1, win, croom)

if __name__ == "__main__":
  main()