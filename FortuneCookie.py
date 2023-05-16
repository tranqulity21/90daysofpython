#a program to tell on someones fortune
import random
question = input("what do you want to know my child?:")
number = random.randint(1,3)
if number == 1:
    print("YES")
elif number == 2:
    print("NO")
elif number == 3:
    print("MAYBE")
else:
    print("don't be ridiculous")
    
