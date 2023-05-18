#dog's info that takes in the dog's name and age and prints a sentence about the dog
def dogs_info(name,age):
  print(f"{name} is {age} years old")
name = input("dog name: ")
age = input("dog age: ")
dogs_info(name,age)

#function that returns all string in uppercase
def uppercase(word):
  return word.upper()

word = input("First name:")
print(uppercase(word))