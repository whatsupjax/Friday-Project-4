# Prompt the user for input to fill in the Mad Lib story
aLargeObject = input("A Large Object: ")
pluralLargeObjects = input("Large Objects (Plural): ")
adjective = input("An Adjective: ")
bodyPart = input("A Body Part: ")
resturant = input("A Resturant: ")
firstFood = input("A Food: ")
secondFood = input("Another Food: ")

# Print the completed Mad Lib story using the user's input
print(
    "I've had a very", adjective, "day.\n"
    "This morning, I dropped a box of", pluralLargeObjects, "on my", bodyPart+".\n"
    "Then, at lunch, I went to", resturant, "for their delicious", firstFood+".\n"
    "But the waiter brought me", secondFood+", which I was not hungry for.\n"
    "Finally, on my way home, I was cut off by a van with a large", aLargeObject, "strapped to the roof."
)