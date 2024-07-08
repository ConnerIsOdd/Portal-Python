from random import randint
from player import *

class Item:
  def __init__(self, name, mindamage, maxdamage, healval, amount):
    self.name = name
    self.mindamage = mindamage
    self.maxdamage = maxdamage
    self.healval = healval
    self.amount = amount

  def __str__(self):
    return f"{self.name}"




class Light_HP_Potion(Item):
  def __init__(self):
    super().__init__("Light HP Potion🧪", 0, 0, 5, 1)
  def __str__(self):
    return f"{self.name}"
  
class Medium_HP_Potion(Item):
  def __init__(self):
    super().__init__("Medium HP Potion🧪", 0, 0, 15, 1)
  def __str__(self):
    return f"{self.name}"
    
class Large_HP_Potion(Item):
  def __init__(self):
    super().__init__("Large HP Potion🧪", 0, 0, 30, 1)
  def __str__(self):
    return f"{self.name}"
    
class Mega_HP_Potion(Item):
  def __init__(self):
    super().__init__("Mega HP Potion🧪", 0, 0, 50, 1)
  def __str__(self):
    return f"{self.name}"
    
class Full_HP_Potion(Item):
  def __init__(self):
    super().__init__("Full HP Potion🧪", 0, 0, 150, 1)
  def __str__(self):
    return f"{self.name}"
    
class Chicken(Item):
  def __init__(self):
    super().__init__("Chicken🍗", 0, 0, 15, 1)
  def __str__(self):
    return f"{self.name}"
    
class Sword(Item):
  def __init__(self):
    super().__init__("Sword⚔️", 5, 20, 0, 1)
  def __str__(self):
    return f"{self.name}"
    
class Dagger(Item):
  def __init__(self):
    super().__init__("Dagger🗡️", 2, 10, 0, 1)
  def __str__(self):
    return f"{self.name}"
    
class Kitchen_Knife(Item):
  def __init__(self):
    super().__init__("Kitchen Knife🔪", 2, 15, 0, 1)
  def __str__(self):
    return f"{self.name}"
  
class Bow(Item):
  def __init__(self):
    super().__init__("Bow🏹", 3, 12, 0, 1)
  def __str__(self):
    return f"{self.name}"
    
class Spiked_Arrow_Bow(Item):
  def __init__(self):
    super().__init__("Spiked Arrow Bow🏹", 4, 15, 0, 1)
  def __str__(self):
    return f"{self.name}"
    
class Baseball_Bat(Item):
  def __init__(self):
    super().__init__("Baseball Bat🏏", 2, 10, 0, 1)
  def __str__(self):
    return f"{self.name}"
  
class Spiked_Baseball_Bat(Item):
  def __init__(self):
    super().__init__("Spiked Baseball Bat🏏", 3, 12, 0, 1)
  def __str__(self):
    return f"{self.name}"
  
class BB_Gun(Item):
  def __init__(self):
    super().__init__("BB Gun🔫", 5, 30, 0, 1)
  def __str__(self):
    return f"{self.name}"
    

class Apple(Item):
  def __init__(self):
    super().__init__("Apple🍎", 0, 0, 2, 1)
  def __str__(self):
    return f"{self.name}"
  

class Corn(Item):
  def __init__(self):
    super().__init__("Corn🌽", 0, 0, 4, 1)
  def __str__(self):
    return f"{self.name}"
  

class Banana(Item):
  def __init__(self):
    super().__init__("Banana🍌", 0, 0, 4, 1)
  def __str__(self):
    return f"{self.name}"
  

class Tomato(Item):
  def __init__(self):
    super().__init__("Tomato🍅", 0, 0, 3, 1)
  def __str__(self):
    return f"{self.name}"