
# Python Fundamentals Lab Assignments

This repository contains solutions for five Python programming labs focused on core programming concepts including user input handling, conditionals, loops, functions, strings, lists, dictionaries, and logical operations.

## Lab 1: The Smart Survey Onboarding Engine

## Overview

This Python program collects user information and automatically assigns an access tier based on predefined business rules. The application demonstrates the use of:


* User input handling
* Data type casting
* Conditional statements
* Boolean logic
* F-Strings for formatted output

---

## Requirements

The program should:

1. Prompt the user for:

   * Name
   * Age
   * Developer Status (`yes` or `no`)

2. Convert input values into appropriate data types:

   * Name → `str`
   * Age → `int`
   * Developer Status → `bool`

3. Apply the following access tier rules:

| Condition                       | Assigned Tier                       |
| ------------------------------- | ----------------------------------- |
| Under 18 years old              | Tier 3: Guest                       |
| 18 or older and Developer       | Tier 1: Admin Infrastructure Access |
| 18 or older and Not a Developer | Tier 2: Standard Executive Access   |

4. Display a personalized configuration summary using an F-String.
5. 
## Example Input

```text
Enter your name: Alice
Enter your age: 25
Are you a developer? (yes/no): yes
```

## Example Output

```text
====================================
User Configuration Summary
====================================
Name: Razeen
Age: 25
Developer: Yes
Assigned Tier: Tier 1: Admin Infrastructure Access
====================================
```

---

## Expected Logic Flow

```text
Start
  ↓
Collect User Information
  ↓
Convert Age to Integer
  ↓
Convert Developer Status to Boolean
  ↓
Is Age < 18?
  ├── Yes → Tier 3: Guest
  └── No
        ↓
   Is Developer?
      ├── Yes → Tier 1: Admin Infrastructure Access
      └── No → Tier 2: Standard Executive Access
  ↓
Display User Summary
  ↓
End
```

---

## Learning Objectives

By completing this exercise, you will practice:

* Taking user input with `input()`
* Type casting using `int()`
* Working with Boolean values
* Using `if`, `elif`, and `else`
* Creating formatted output using F-Strings
* Implementing business logic in Python

---

## Technologies Used

* Python 3.x

