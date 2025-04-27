# Singleton
The Singleton pattern ensures that a class has only one instance, and provides a global point of access to it.
![alt text](image.png)

## ✅ It Solves Two Problems

### 1. Ensure that a class has just a single instance.
Why? Because sometimes, creating more than one of something could cause issues or waste resources.

Example: A database connection. You typically want only one connection manager in the app, not multiple conflicting ones.

So, with Singleton, if you try to "make another one," you actually get the original one you already created.

❗️This behavior is impossible to implement using a regular constructor, since it always returns a new object by design.

🔁 Singleton pattern bypasses this by intercepting the creation process and reusing the existing instance instead of making a new one.

### 2. Provide a Global Access Point
Global variables are easy to access from anywhere in your program. While convenient, they’re also risky: any part of the code can overwrite them, leading to unpredictable behavior or crashes.

The Singleton pattern offers a safer alternative. Like a global variable, the Singleton allows global access to an object. But unlike a global variable, the Singleton protects that instance from being overwritten or accidentally recreated.

There’s another side to this problem: you don’t want the logic that ensures only one instance exists to be scattered throughout your code. It’s much cleaner and more maintainable to centralize that logic within a single class—especially if your application already depends on that class for something important.

So you get:

🌍 One shared instance across the app.

🛡️ Protection from being accidentally re-created or overwritten.

## 🤯 SRP Violation
SRP = Single Responsibility Principle

One class should do one thing. Singleton pattern technically mixes two responsibilities into one class:

1. Manage instance control (creation, existence, etc.)

2. Provide business logic (whatever the object is actually for logging, database access, etc.)

## 📌 Recap
Singleton = One instance + Global access

- Prevents multiple instances of a class

- Gives you a single place to access a shared resource

- Safer than global variables

- Slight downside: breaks SRP
