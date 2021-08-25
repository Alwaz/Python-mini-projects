import random

def guess(ending_range):
    randome_range=random.randint(1,ending_range)
    guess = 0
    while guess!=randome_range:
        guess = int(input("Enter a numnber between 1 and "+ str(ending_range)))
        if guess > randome_range:
            print("Sorry! try again guess id too high")
        elif guess<randome_range:
            print("Sorry wrong guess it is too low")



    print("yay! you havr guessed the number "+ str(randome_range) + " correctly")

print(guess(50))