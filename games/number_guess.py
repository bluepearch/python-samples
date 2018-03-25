import random

number_to_guess = random.randint(1, 10)

user_guess = 500

while user_guess != number_to_guess:
  user_guess = int(input("What is my number?"))
  print("You guessed: " + str(user_guess))
  if user_guess == number_to_guess:
     print("You Win!!!!")
  elif user_guess > number_to_guess:
     print("Too High!")
  elif user_guess < number_to_guess:
     print("Too Low!")
  else:
     print("Wrong! try again!")
  
