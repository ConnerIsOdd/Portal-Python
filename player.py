from random import randint


class Player:
  def __init__(self, name, weapon):
    self.name = name
    self.MHP = 150
    self.HP = self.MHP
    self.weapon = weapon
    self.inventory = [self.weapon]
    self.x = 0
    
    

  def __str__(self):
    return f"Name: {self.name}\nHP: {self.MHP}\nAttack Power: {self.AP}\nWeapon: {self.weapon}\nInventory: {self.inventory}"
    
  def AP():
    num = randint(0, 5)
    if num == 0:
      AP = 1
      return AP
    elif num == 1:
      AP = 1.1
      return AP
    elif num == 2:
      AP = 1.2
      return AP
    elif num == 3:
      AP = 1.3
      return AP
    elif num == 4:
      AP = 1.4
      return AP
    elif num == 5:
      AP = 1.5
      return AP

    

  def heal(self, num):
    if self.HP + num <= self.MHP:
      self.HP = self.HP + num

    elif self.HP + num >= self.MHP:
      self.HP = self.MHP

  def take_damage(self, num):
    if self.HP - num > 0:
      self.HP = self.HP - num

    elif self.HP - num <= 0:
      self.HP = 0


  def remove_item(self, item):
    if item in self.inventory:
      self.inventory.remove(self.inventory.index(item))

    else:
      print("\nInvalid Item")
    
    
  

  