import random
jackpot=random.randint(1,100)
counter=1
name=input("Enter your name:")
guess=int(input("Enter your guess="))

while guess!=jackpot:  
  counter=counter+1;
  if guess<jackpot:
    print("INCORRECT, GUESS HIGHER....")
    guess=int(input("Enter your guess again="))
  else:
    print("INCORRECT, GUESS LOWER...")
    guess=int(input("Enter your guess again="))
print("CONGRATS",name,"you took",counter,"attempts")
