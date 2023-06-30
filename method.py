#method is a function inside a class
#showcase a method that uses one of yoyur instance variables
import random
class Dog:
  def __init__(self, name):
    print("Teeshah kennels")
    self.name = name
    self.puppy_age = random.randint(1,10)
  #method that uses instance variables  
  def bark(self):
    print(f"aouf! i'm {self.name} and i'm {self.puppy_age} years")
    
dog1 = Dog("cookie")
dog2 = Dog("mace")
#calling object dog1/dog2 to execute the method bark()
dog1.bark()
dog2.bark()
