from random import randint


class Enemy:
  def __init__(self, name, MHP, mindamage, maxdamage):
    self.name = name
    self.MHP = MHP
    self.HP = MHP
    self.mindamage = mindamage
    self.maxdamage = maxdamage

  def __str__(self):
    return f"{self.name}"
def damage_determination(self, num1, num2):
  Damage = randint(num1, num2)
  return Damage

def take_damage(self, num):
  if self.HP - num > 0:
    self.HP = self.HP - num

  elif self.HP - num <= 0:
    self.HP = 0

    
class Fragmented_Corrupted_Portal(Enemy):
  def __init__(self):
    super().__init__("Fragmented Corrupted Portal", 60, 10, 30)

class Corrupted_Travelers(Enemy):
  def __init__(self):
    super().__init__("Corrupted Traveler", 35, 5, 15)

class Soul_Skeletons(Enemy):
  def __init__(self):
    super().__init__("Soul Skeleton", 20, 1, 5)

class Blood_Boilers(Enemy):
  def __init__(self):
    super().__init__("Blood Boiler", 15, 1, 15)

class Skin_Stealers(Enemy):
  def __init__(self):
    super().__init__("Skin Stealer", 30, 1, 15)
  
    