# Design patterns
This repository contains all the notes and knowledge learned during my journey of discovering and exploring design patterns.

## I.	Intro
Design patterns are reusable solutions to common problems that arise during software development.

They represent distilled wisdom from countless software projects, offering solutions that have stood the test of time and continue to guide modern software architecture.

The concept was introduced by the 1994 book "Design Patterns: Elements of Reusable Object-Oriented Software".

## II.	PROs - CONs
The best software engineers understand when to apply design patterns and when a simpler solution might be more appropriate.

The key is to view patterns as tools in your toolkit rather than mandatory solutions for every problem.

### A.  PROs
| Advantage              | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| Proven Solutions       | Refined by multiple experienced developers over years of practice on various projects.        |
| Collaboration          | Standardized terminology to communicate complex design ideas concisely and accurately.         |
| Speed                  | Using ready-made templates can reduce development time.                                       |
| Code Reusability       | Creation of reusable components across different projects and contexts.                        |
| Maintainability        | More organized, modular code that's easier to understand and maintain.                         |
| Scalability            | Designed to help applications scale efficiently as requirements grow.                          |
| Adaptability           | Specifically designed to make systems more adaptable to future changes.                       |

### B.  CONs
| Disadvantage               | Description                                                                                                               |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Complexity                 | May introduce unnecessary complexity if applied to simple problems or used prematurely (over-engineering).               |
| Misapplication             | Using the wrong pattern for a given problem can create more issues than it solves.                                       |
| Learning Curve             | Understanding when and how to apply patterns correctly requires significant experience and study.                        |
| Readability                | Requires additional classes and interfaces, potentially increasing codebase size.                                        |
| Creativity Limitation      | Over-reliance on patterns may limit creative problem-solving and encourage “pattern-oriented” rather than “problem-oriented” thinking. |
| Context Insensitivity      | Patterns developed in one context (like object-oriented languages) may not translate well to other paradigms or languages.|
| Performance Impact         | Adding abstraction layers can affect application performance.                                                             |

## III.	Categories
There are 22 design patterns and they generally fall into three main categories:

### 1. Creational Patterns
Object creation mechanisms. They abstract the instantiation process, making systems independent of how their objects are created, composed, and represented.

- **Singleton:** Ensures a class has only one instance and provides a global point of access to it.
- **Factory Method:** Creates objects without specifying the exact class of object that will be created.
- **Builder:** Separates the construction of a complex object from its representation.
- **Prototype:** Creates new objects by copying an existing object.

### 2. Structural Patterns
Object composition mechanisms. How classes and objects are composed to form larger structures, focusing on simplifying the structure by identifying relationships.

- **Adapter:** Allows incompatible interfaces to work together.
- **Composite:** Composes objects into tree structures to represent part-whole hierarchies.
- **Decorator:** Attaches additional responsibilities to objects dynamically.
- **Facade:** Provides a simplified interface to a complex subsystem.

### 3. Behavioral Patterns
Object communication mechanisms. It concerns algorithms and the assignment of responsibilities among objects.

- **Observer:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified.
- **Strategy:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
- **Command:** Encapsulates a request as an object, allowing for parameterization of clients with different requests.
- **Iterator:** Provides a way to access elements of a collection sequentially without exposing its underlying representation.
