import random

# Initialize variables to keep track of correct and incorrect answers
correct = 0
incorrect = 0

# Define a dictionary containing questions and their answers
questionBank = {
    "Who is the professor of DS3650?": "Dr. Clary",
    "What is the mascot of TTU?": "Golden Eagle",
    "Where are business classes located on campus?": "Foundation Hall",
    "What is the course number for this class?": "DS3850",
    "What grade are you considered when you begin college?": "Freshman"
}

# Loop through each question in the question bank
for question in questionBank:
    # Print the question
    print(question)
    # Get the user's answer
    answer = input("ANSWER: ")
    # Check if the answer is correct
    if answer == questionBank[question]:
        # If correct, print a message and increment the correct count
        print("That is correct.")
        correct += 1
    else:
        # If incorrect, print a message, increment the incorrect count, and print the correct answer
        print("That is incorrect.")
        incorrect += 1
        print("The correct answer is:", questionBank[question])

# Print the user's score
print("Your score is:", str(correct) + "/" + str(incorrect))
