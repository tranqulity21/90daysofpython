#Instructions:
#computer should guess a number between 1 and 100
#The program should prompt the user to input what number they guessed
#A range should be given to tell the user whether they guessed higher or lower
#When the user's guess is wrong the program should prompt him again till the correct answer is gotten
import random
import time
print("WELCOME TO THE GUESSING GAME!!!I SILL THINK OF A NUMBER BETWEEN 1 AND 100 AND YOU WILL TELL ME WHAT IT IS")
print("guessing a number...")
#time.sleep() this function delays the execution for a defined time,just to make the machine see, alive
time.sleep(2)
guess = int(input("Done!what's your guess:"))
#random generator that generates numbers between 1 and 100
comp_guess = random.randint(1,100)
#guess_count variable checks how many times the code has been run to indicate number of tries
guess_count = 1
#the while loop runs as long as condition is not met
while guess != comp_guess:
#the if else loop is used in comparison to make it easier for a user to know where the correct number range lies 
  if guess > comp_guess:
    print("checking...")
    time.sleep(1)
    guess = int(input("sorry too high,guess again:"))
  else:
    print("checking...")
    time.sleep(1)
    guess = int(input("sorry too low,guess again:"))
  guess_count+=1

print(f"Woah so smart!!!you got it after {guess_count} guesses!")