# Friday-Project-4
Project 1
This Python code is a simple Mad Libs game that prompts the user to enter various words and phrases to fill in the blanks of a predefined story template. Here's a detailed breakdown of how the code works:

User Input: The program uses the input() function to prompt the user to enter specific types of words or phrases, such as a large object, plural large objects, an adjective, a body part, a restaurant name, and two different types of foods.

Variable Assignment: Each user input is stored in a separate variable (aLargeObject, pluralLargeObjects, adjective, bodyPart, restaurant, firstFood, secondFood) for later use in the Mad Lib story.

Story Construction: The print() function is used to construct the Mad Lib story using a series of concatenated strings and the user-input variables. The story is formatted with line breaks (\n) to make it more readable.

Output: The completed Mad Lib story is printed to the console, incorporating the user's input to create a unique and often humorous story each time the program is run.

Overall, this code demonstrates basic input/output operations in Python and showcases how user input can be used to dynamically generate text-based content.

Project 2
This Python code simulates a simple Power Ball game. Here's a detailed description of what each part of the code does:

Imports: The code begins by importing the random module to generate random numbers and the time module to introduce delays in the output.

Initialization: It initializes a variable iteration to keep track of the number of iterations in a loop.

User Input: The code prompts the user with the question "Do you want to play the Power Ball? (Y/N)" and stores the user's response in the variable doYouWantToPlay.

Check User Input: It checks if the user wants to play (doYouWantToPlay == "Y"). If the user chooses to play, the game continues; otherwise, it prints "Maybe next time..." and exits.

Age Verification: If the user chooses to play, the code asks for the user's age and stores it in age. It then converts age to an integer and stores it in oldEnough.

Age Check: It checks if the user's age (oldEnough) is 18 or older. If the user is not old enough, it prints "You aren't old enough buddy." and exits the game.

Game Play: If the user is old enough, it prints "Below are your winning numbers!" and enters a loop that runs five times (while iteration < 5). In each iteration, it generates a random number between 1 and 69 using random.randint(1, 69) and prints the number. It then increments iteration by 1 and introduces a 1-second delay using time.sleep(1).

Power Number: After printing the five numbers, it prints "POWER NUMBER!" and introduces a 2-second delay using time.sleep(2). It then generates a random power number between 1 and 26 using random.randint(1, 26) and prints the power number.

Game End: Finally, it prints "Thanks for playing! May the odds be in your favor." and exits the game.

This code provides a basic simulation of a Power Ball game, where the user can choose to play, enter their age to verify eligibility, and then receive randomly generated winning numbers.

Project 3
It imports the random module, although it's not used in the provided code snippet.

It initializes two variables, correct and incorrect, to keep track of the number of correct and incorrect answers, respectively.

It defines a dictionary called questionBank that maps questions to their corresponding answers. Each question-answer pair represents a quiz question.

It iterates over each question in the questionBank dictionary using a for loop.

For each question, it prints the question to the console and waits for user input using the input function. The user's input is stored in the answer variable.

It checks if the user's answer (answer) matches the correct answer stored in the questionBank dictionary for the current question (question). If the answers match, it prints "That is correct." and increments the correct variable. If the answers do not match, it prints "That is incorrect.", increments the incorrect variable, and prints the correct answer.

After iterating through all the questions, it prints the user's score by concatenating the correct and incorrect counts.

Overall, the code implements a simple quiz program that asks the user a series of questions and provides feedback on the correctness of their answers. At the end of the quiz, it displays the user's score.