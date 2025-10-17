# 💬 Interactive System (Python OOP)

A simple **Python Object-Oriented Programming (OOP)** project that demonstrates how to use **classes**, **objects**, and **user input** to create interactive console applications.

---

## 🧠 Overview

The **Interactive System** asks the user for their **name** and **age**, stores this information inside a class object, and displays a personalized greeting message.

This project is ideal for beginners learning how to:
- Create and initialize classes in Python
- Instantiate objects
- Work with user input and formatted output
- Apply basic OOP principles in small programs

---

## 🧩 Code Example

```python
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
```

# 💻 Example Output

```vbnet


What's your name?
Moisés
Your age:
20

Moisés 

20 

==================== Welcome to our system! ===================== 

Hello Moisés! Thank you for interacting with us. 
Your age is: 20. 
See you later!
=================================================================
```

# ⚙️ How It Works
* The program defines a class called Interactive with two attributes:

- user: stores the user’s name.

- age: stores the user’s age.

* The program collects input from the user using the input() function.

* It then creates an object (interactive) from the Interactive class.

* Finally, it displays personalized messages using the stored data.

# 🧾 Key Concepts

* Covered Concepts :

Class: 	A blueprint for creating objects with attributes and methods.
Object (Instance): 	A specific realization of a class, with actual data.
__init__ Method: 	A constructor that initializes an object’s attributes.
Attributes	Variables: that belong to an object.
User Input:	Collects information from the user in real time.

🚀 How to Run
Make sure you have Python 3.10+ installed.

Save the file as system.py.

Open a terminal in the same folder and run:

bash
Copiar código
python system.py
📘 Author
Moisés
🎯 Python Developer | Learning Object-Oriented Programming
💬 “See you later!” 😄
