
# Python Fundamentals Lab Assignments

This repository contains solutions for five Python programming labs focused on core programming concepts including user input handling, conditionals, loops, functions, strings, lists, dictionaries, and logical operations.

## Lab 1: The Smart Survey Onboarding Engine

This Python program collects user information and automatically assigns an access tier based on predefined business rules


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


* Taking user input with `input()`
* Type casting using `int()`
* Working with Boolean values
* Using `if`, `elif`, and `else`
* Creating formatted output using F-Strings

---

# Lab 2: The Multi-Cluster IP Audit Tool


The Multi-Cluster IP Audit Tool is a Python program that analyzes a cloud cluster configuration and calculates infrastructure utilization. 

---


## Features

* Reads data from a nested dictionary structure
* Counts active nodes using a loop
* Calculates cluster utilization percentage
* Displays a formatted infrastructure report

---

## Configuration Example

```python
cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": [
        "10.0.1.15",
        "10.0.1.16",
        "10.0.1.17",
        "10.0.1.18",
        "10.0.1.19"
    ]
}
```

---

## Utilization Formula

```text
Utilization % = (Active Nodes / Total Max Slots) × 100
```

For the provided configuration:

```text
Active Nodes = 5
Total Max Slots = 8

Utilization % = (5 / 8) × 100 = 62.5%
```

---

## Expected Output

```text
Cluster Name: dhaka-prod-east
Active Nodes: 5
Total Capacity: 8
Cluster Utilization: 62.50%
```

---

## Learning Objectives

* Work with Lists (`list`) and Dictionaries (`dict`)
* Use Sequential Loops (`for`)
* Calculate Percentages

---

## How to Run

1. Save the script as `lab1_SmartSurvey.py`
2. Save the script as `lab2_ClusterAudit.py`
3. Save the script as `lab3_BudgetOptimizer.py`
4. Save the script as `lab4_TextNormalization.py`
5. Save the script as `lab5_AlertFlagEvaluator.py`
6. Open a terminal in the project directory.
3. Execute:

```bash
python lab1_SmartSurvey.py
python lab2_ClusterAudit.py
python lab3_BudgetOptimizer.py
python lab4_TextNormalization.py
python lab5_AlertFlagEvaluator.py
```

---

## Technologies Used

* Python 3.x

