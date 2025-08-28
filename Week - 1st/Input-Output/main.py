# Ask the user for their name
name = input("What is your name? ")
print("Hello,", name, "! Welcome to Python.")


# --- Simple Addition Program ---
# Take the first number from the user and convert it to an integer
num1 = int(input("Enter first number: "))

# Take the second number from the user and convert it to an integer
num2 = int(input("Enter second number: "))

# Add the two numbers and store the result
result = num1 + num2

# Display the sum of the two numbers
print("The sum is:", result)


# --- String Operations ---
# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase
print("Uppercase:", sentence.upper())

# Convert the sentence to lowercase
print("Lowercase:", sentence.lower())

# Count how many characters are in the sentence
print("Number of characters:", len(sentence))
