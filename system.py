class Interactive:
    def __init__(self, user, age):
        self.user = user
        self.age = age


# Ask user for input
user = input("What's your name? \n")
age = input("Your age: \n")

# Create an instance
interactive = Interactive(user, age)

# Access attributes from the instance
print(interactive.user, "\n")
print(interactive.age, "\n")

print("==================== Welcome to our system! ===================== \n")
print(f"Hello {interactive.user}! Thank you for interacting with us. \n")
print(f"Your age is: {interactive.age}. \n")
print("See you later!")
print("=================================================================")
