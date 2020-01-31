import random
n = random.randint(1, 99)
guess = int(raw_input("Enter a number from 1 to 99: "))
while n != "guess":
    print
    if guess < n:
        print "guess is wrong"
        guess = int(raw_input("Enter a number from 1 to 99: "))
    elif guess > n:
        print "guess is high"
        guess = int(raw_input("Enter a number from 1 to 99: "))
    else:
        print "you guessed it!"
        break
    print