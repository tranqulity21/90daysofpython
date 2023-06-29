mport random
class Dog:
  Breed = "SouthAfrican Boerboel";
  info = "The Boerboel is a large, muscular working breed from South Africa known for its loyalty, protective nature, and confident temperament"
#function runs everytime an object is created from the class
  def __init__(self):
    print("Teeshah kennels")
    print(random.randint(1,10))
  
print(Dog.Breed)
print(Dog.info)

#instance or object -whenever you create somethng from a class 
#each objects are different from one another,observe through the rand int generator
Dog()
Dog()
Dog()
