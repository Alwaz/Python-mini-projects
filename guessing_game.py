import random


# we will guess
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



# Computer will guess here
def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback= ""



    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input("Is the number "+ str(guess) + " is too high (h), too low(l) or is it correct (c) ")
        if feedback == 'h':
            high=guess
        elif feedback == 'l':
            low=guess+1
    print("Thank God I finally guessed it")


computer_guess(10)