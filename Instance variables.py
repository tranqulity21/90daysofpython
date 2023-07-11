#create instance variables through 2 ways
#1.inside the init function
#2.after object is created
import random
class Dog:
  Breed = "SouthAfrican Boerboel";
  info = "The Boerboel is a large, muscular working breed from South Africa known for its loyalty, protective nature, and confident temperament"
#function runs everytime an object is created from the class
  def __init__(self):
    print("Teeshah kennels")
#instance variable TYPE 1
    self.puppy_number = (random.randint(1,10))
  
print(Dog.Breed)
print(Dog.info)#access class variable

dog1 = Dog()
dog2 = Dog()

#instance variables are individual to a particular object

#creating instance class afterobject is created TYPE 2
dog1.name = "Cookie"
print(dog1.name)
