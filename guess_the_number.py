import random
def guess():
 if b > a:
  print("Your number is too big!")
 else :
  print("Your number is too small!")

number = input("Guess a number between 0 and 20: ")
b = int(number)

a = random.randint(0 , 20)


while a!=b:
    guess()
    print("The number I was thinking is: " + str(a))
    number = input("guess again: ")
    b = int(number)
else:
    print("You guessed the number!!!")