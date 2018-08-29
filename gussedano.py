import random
random_no = random.randrange(0,100)
print("Random number has been generated from 0 to 100\n")
guessed=False
while guessed==False:
    user_input = int(input("Your guess a no please from 0 to 100: "))
    if user_input==random_no:
        guessed = True
        print("Well done!")
    elif user_input>100:
        print("Our guess range is between 0 and 100, please try a bit lower no\n")
    elif user_input<0:
        print("Our guess range is between 0 and 100, please try a bit higher no\n")
    elif user_input>random_no:
        print("Try one more time, a bit lower no\n")
    elif user_input < random_no:
        print("Try one more time, a bit higher no\n")

print("End of program")