import random
import time

# Initialize a variable to keep track of the number of iterations in the while loop
iteration = 0

# Ask the user if they want to play the Power Ball
doYouWantToPlay = input("Do you want to play the Power Ball? (Y/N)\n")

# Check if the user wants to play
if doYouWantToPlay == "Y":
    print("Lets get started!")
    
    # Ask the user for their age
    age = input("What is your age?\n")
    oldEnough = int(age)
    
    # Check if the user is old enough to play
    if oldEnough >= 18:
        print("Below are your winning numbers!")
        
        # Generate and print the first five random numbers
        while iteration < 5:
            number = random.randint(1, 69)
            print(number)
            iteration += 1
            time.sleep(1)
        
        # Generate and print the power number
        print("POWER NUMBER!")
        time.sleep(2)
        powerNumber = random.randint(1, 26)
        print(powerNumber)
        
        # End of the game message
        print("Thanks for playing! May the odds be in your favor.")
    
    # Display a message if the user is not old enough to play
    else:
        print("You aren't old enough buddy.")
else:
    # Display a message if the user chooses not to play
    print("Maybe next time...")
