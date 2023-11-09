import random

num = random.randint(1,100)
count = 1
chances = 3

start = input("Do you want to play Number Guessing Game? Answer Y or N")

if start == 'Y':
    print("Okay lets Start the Game")
    print("I have a number between 1-100, try to guess it..")
    while chances >= 1:
        guess = int(input("Guess The Number"))
        if guess > num:
            print("Your guess is little high, guess lower nummber than",guess)
        elif guess < num:
            print("Your guess is little low, guess heigher nummber than",guess)
        else:
            print("Hooorayyyy....")
            print("You guessed the correct number")

            break
        chances -=1
        print(chances , "Chnaces left")
        count +=1
    print("GAME OVER")
    print("Number is ", num)
    print('Thanks for playing')
elif start == "N":
    print("oaky, if you would like to play visit again")
else:
    print("Sorry, I didnt get you")