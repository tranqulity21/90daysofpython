class Dog:
#everytime that you make a dog you wanna make sure it has a name,pass name parameter
  def __init__(self, name):
    print("Teeshah kennels")
#instance variable
    #take name passed in and put it in a variable
    self.namevar = name 

dog1 = Dog("cookie")
dog2 = Dog("mace")

#instance variables are individual to a particular object

#creating instance class afterobject is created
print(dog1.namevar)
print(dog2.namevar)
