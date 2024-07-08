from random import choice, randint, shuffle
from items import *
from player import Player
from enemies import *
from time import sleep
from enemies import *
from colorama import Fore
from sys import exit

Blue = Fore.BLUE
Green = Fore.GREEN
Yellow = Fore.YELLOW
Red = Fore.RED
Magenta = Fore.MAGENTA
Black = Fore.BLACK
White = Fore.WHITE
Cyan = Fore.CYAN

class Map:
  def map_gen(self):
    map = []
    for i in range (0, 16):
      num = randint(1, 10)
      if num == 1:
        portal = Empty_Room()
      elif num == 2 or num == 6:
        portal = Enemy_Room()
      elif num == 3 or num == 7:
        portal = Treasure_Room()
      elif num == 4 or num == 8 or num == 9:
        portal = Puzzle_Room()
      elif num == 5:
        portal = Portal_Inside_Portal_Room()
      map.append(portal)
    map[0] = Start_Room()
    map[15] = Stop_Room()
    return map
  def __getitem__(self, i):
    return self.map[i]

  def __init__(self):
    self.map = self.map_gen()

  def __str__(self):
    return f"{self.map}"


class Empty_Room():
  def __init__(self):
    self.room = "empty"

  def __str__(self):
    return f"{self.room}"

  def empty(self):
    print("\nThe Portal Takes You Into A Empty Room With Another Portal")
    sleep(0.7)
    print("You Go Into The Portal")
    sleep(0.7)
    win = True
    return win

class Enemy_Room():
  def __init__(self):
    self.room = "enemy"

  def __str__(self):
    return f"{self.room}"
  
  def battle(self, P1):
    num = randint(1, 5)
    if num == 1:
      enemy = Fragmented_Corrupted_Portal()

    if num == 2:
      enemy = Corrupted_Travelers()

    if num == 3:
      enemy = Soul_Skeletons()

    if num == 4:
      enemy = Blood_Boilers()

    if num == 5:
      enemy = Skin_Stealers()
      
    print("The Room Your In Has No Portal.")
    sleep(2)
    print(f"You Walk Forward And Encounter A", Red + f"{enemy.name}!" + White)
    sleep(2)
    while P1.HP > 0:
      if enemy.HP > 0:
          print("What Will You Do?\n\n  1-", Red + "Attack", White + "\n  2-", Cyan + "Heal" + White)
          choice = input(Yellow + "\ninput Choice Here: " + White)
          try:
            choice = int(choice)
          except:
            print("\nYou Panic And Do Nothing!")
          if choice == 1:
              damage = randint(P1.weapon.mindamage, P1.weapon.maxdamage)
              print("\nYou Decide To", Red + "Attack!" + White)
              sleep(1)
              enemy.HP -= damage
              print(f"\nThe ", Red + f"{enemy.name}", White + f"Lost {damage}", Cyan + "HP!" + White)
          elif choice == 2:
              print("\nYou Chose To ", Cyan + "Heal!" + White)
              sleep(1)
              Heals = []
              for i in P1.inventory:
                if i.healval > 0:
                    Heals.append(i)
              if len(Heals) > 0:
                print("\nChoose A ", Cyan + "Heal:" + White)
                num = 0
                for i in range(0, len(Heals) - 1):
                  print(f"\n{num}- {Heals[i]}")
                  num += 1
                  
                choice = input(Yellow + "\nInput Choice Here: " + White)
                try:
                  choice = int(choice)
                  HPamm = Heals[choice].healval
                  P1.inventory.remove(Heals[choice])
                  P1.heal(HPamm)
                  print(f"\nYou ", Cyan + "Healed", White + f"{HPamm}")
                except:
                  print(Red + "\nInvalid Choice:", White + "You", Red + "Panic", White + "And Do Nothing!")
                
      
              else:
                print("\nYou Have No", Cyan + "Heals!" + White)
              
              
      
          
    
          if enemy.HP <0:
            enemy.HP = 0
          elif enemy.HP > 0:
            print(f"\nThe ", Red + f"{enemy.name}", White + "Attacks You!")
            damage = randint(enemy.mindamage, enemy.maxdamage)
            P1.take_damage(damage)
            sleep(0.4)
            print(f"\nYou Took", Red + f"{damage}" + White)
            print("".center(30, '-'))
            sleep(0.5)
            print(f"Your", Cyan + f"HP: {P1.HP}\n\n", White + "The", Red + f"{enemy.name}'s", Cyan + f"HP: {enemy.HP}\n" + White)
            print("".center(30, '-'))
    
        
      if enemy.HP == 0:
        print(f"\nYou Killed The", Red + f"{enemy.name}!" + White)
        sleep(0.7)
        print("\nA Portal Appears, You Go Through It.")
        win = True
        return win

    if enemy.HP > 0:
      print(f"\nYou Lost, The", Red + f"{enemy.name}", White + "Takes Your Life...")
      win = False
    return win
####################################################3
class Treasure_Room():
  def __init__(self):
    self.room = "Treasure"

  def __str__(self):
    return f"{self.room}"

  def treasure(self, P1):
    print("\nYou Find A", Yellow + "Chest!" + White)
    sleep(2)
    print("\nYou Open It And You Find: ")
    sleep(1)
    num2 = randint(1, 6)
    for i in range(num2):
      sleep(1)
      num3 = randint(1, 10)
      if num3 == 1:
          P1.inventory.append(Light_HP_Potion())
          print("\n  -Light HP Potion🧪")

      elif num3 == 2:
          P1.inventory.append(Medium_HP_Potion())
          print("\n  -Medium HP Potion🧪")
      elif num3 == 3:
          P1.inventory.append(Large_HP_Potion())
          print("\n  -Large HP Potion🧪")
      elif num3 == 4:
          P1.inventory.append(Mega_HP_Potion())
          print("\n  -Mega HP Potion🧪")
      elif num3 == 5:
          P1.inventory.append(Full_HP_Potion())
          print("\n  -Full HP Potion🧪")
      elif num3 == 6:
          P1.inventory.append(Chicken())
          print("\n  -Chicken🍗")
      elif num3 == 7:
          P1.inventory.append(Apple())
          print("\n  -Apple🍎")
      elif num3 == 8:
          P1.inventory.append(Corn())
          print("\n  -Corn🌽")
      elif num3 == 9:
          P1.inventory.append(Banana())
          print("\n  -Banana🍌")
      elif num3 == 10:
          P1.inventory.append(Tomato())
          print("\n  -Tomato🍅")
    sleep(2)
    win = True
    return win




class Start_Room():
  def __init__(self):
    self.room = "Start"

  def __str__(self):
    return f"{self.room}"

class Stop_Room():
  def __init__(self):
    self.room = "Stop"

  def __str__(self):
    return f"{self.room}"

class Puzzle_Room():
  def __init__(self):
    self.room = "Puzzle"
    
  def __str__(self):
    return f"{self.room}"
  
  def puzzle_random_puzzle1(self, P1):
    code = str(randint(100, 999))
    digits = [*code]
    print("\nAfter Searching, You Find The Next Portal")
    sleep(2)
    print("\nBut It Needs A Code To Be Activated")
    sleep(2)
    print("\nThe Code Is 3 Numbers.")
    sleep(2)
    num = randint(1, 3)
    if num == 1:
      print("\nThe Portal Reveals The First And Last Numbers")
      print(f"\nThose Numbers Are {digits[0]} And {digits[2]}")

    elif num == 2:
      print("\nThe Portal Reveals The First Number")
      print(f"\nThat Number is {digits[0]}")

    if num == 3:
      print("\nThe Portal Reveals All 3 Numbers But Unordered")
      print(f"\nThose Numbers Are {digits[1]}, {digits[0]} and {digits[2]}")

    guess = input(Yellow + "\nWhat Is The Code: " + White)
    if guess == code:
      print(Green + "\nCorrect!" + White)
      sleep(2)
      print("\nThe Portal Opens, Taking You To The Next Room!, It Also Heals You!")
      P1.HP += randint(5, 20)
      win = True

    elif guess != code:
      print(Red + "\nIncorrect!" + White)
      sleep(1)
      print("\nThe Portal Transforms Into Another Portal!")
      sleep(1)
      print("\nIt Sucks You In! You Lost Some Of Your", Cyan + "HP", White + "From Force!")
      HPsubtract = randint(5, 30)
      P1.take_damage(HPsubtract)
      print(f"\nYou Lost {HPsubtract}", Cyan + "HP", White + f"!\nYou Now Have {P1.HP}", Cyan + "HP" + White)
      win = False

  def puzzle_random_puzzle2(self, P1):
    win = None
    luck = ["good", "average", "bad"]
    shuffle(luck)
    portalchoices = ["Red", "Blue", "Green"]
    print("\nAfter Searching, You Find 3 Portals!")
    sleep(2)
    print("\nOne, Is", Red + "Red", White + ", One Is", Blue + "Blue", White + ", And One Is", Green + "Green." + White)
    sleep(2)
    print("\nWhich One Do You Go Through?\n  1-", Red + "Red ", White + "Portal\n  2-", Blue + "Blue ", White + "Portal\n  3-", Green + "Green ", White + "Portal")
    choice = input(Yellow + "\nInput Choice Here: " + White)
    try:
      choice = int(choice)
      if choice <4 and choice >0:
        print(f"\nYou Chose The {portalchoices[choice-1]} Portal")
        luckchoice = luck[choice-1]
        if luckchoice == "good":
          sleep(2)
          heal = randint(2, 21)
          print(f"\nA Portal Appears And", Cyan + "Heals", White + f"{heal}", Cyan + "HP!" + White)
          P1.heal(heal)
          sleep(2)
          print("\nYou Go Through The Portal")
          sleep(2)
          
    
        elif luckchoice == "average":
          sleep(2)
          print("\nYou Go Through The Portal")
          sleep(2)
          print("\nIt Takes You To The Next Room!")
          win == True
    
        elif luckchoice == "bad":
          sleep(2)
          print("\nYou Go Through The Portal.")
          sleep(2)
          print("\nIt Takes You To Another Room That Is Not The Next One!")
          win == False
    
    
    
      else:
        print("\nYou", Red + "Panic", White + "Because You Can't Decide And The Portal", Red + "Kills You!" + White)
        input("Press Enter To Exit: ")
        exit()
    except:
      print("\nYou", Red + "Panic", White + "Because You Can't Decide And The Portal", Red + "Kills You!" + White)
      input("Press Enter To Exit: ")
      exit()
    return win
  
  def puzzle_random_puzzle3(self, P1):
    win = None
    print("\nYour In A Room With A D6 Dice🎲.")
    sleep(2)
    print("\nWith Nothing Else In This Empty Room, You Decide To Roll It Out Of Curriosity.")
    sleep(2)
    input("\nPress Enter To Roll: ")
    print("\nRolling🎲...")
    sleep(2)
    num = randint(1, 6)
    print(f"\nYou Landed A {num}!")
    sleep(2)
    if num == 1:
      num == randint(3, 20)
      print("\nA Portal Appears Right Where You Are, Causing It To", Red + "Push", White + f"You Into The Wall, You Lose {num}", Cyan + "HP!" + White)
      P1.take_damage(num)
      sleep(2)
      print("\nEven Though The Portal", Red + "Hurt", White + "You, You Still Decide To Go Through It.")
      sleep(2)
      win == True
    elif num == 2:
      print("\n2 Closed Portals Appear Where You Are, Causing Them To", Red + "Crush You To Death" + White)
      sleep(2)
      input("\nPress Enter To Exit: ")
      exit()

    elif num == 3:
      print("\nA Portal Appears In Front Of You, You Go Through It.")
      sleep(2)
      win == True

    elif num == 4:
      sleep(0.7)
      win == True

    elif num == 5:
      print("\nNothing Happens, Nothing Appears...")
      sleep(1)
      print("\nYou Just Sit There, Playing with The Dice In This Void Type Room")
      sleep(1)
      print("\nAfter 3 Days, You Can't Move, Your Paralyzed...")
      sleep(1)
      print("\nNo Food...")
      sleep(1)
      print("\nNo Water...")
      sleep(1)
      print("\nYou Slowly", Red + "Pass Away..." + White)
      sleep(1)
      input("\nPress Enter To Exit: ")
      exit()


    elif num == 6:
      print("\nYou Blink, Then Dissapear Into Another Portal.")
      sleep(0.7)
      win == True
      
    return win
    
class Portal_Inside_Portal_Room():
  def __init__(self):
    self.room = "Portal Inside Portal"

  def __str__(self):
    return f"{self.room}"

  def portal_inside_portal(self):
    print("\nThe Portal Takes You Into A Empty Room With Another Portal")
    sleep(2)
    print("You Go Into The Portal")
    sleep(2)
    win = True
    return win





  


  
          
  
  
  