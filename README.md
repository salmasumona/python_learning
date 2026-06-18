
# Python Fundamentals Lab Assignments

This repository contains solutions for five Python programming labs focused on core programming concepts including user input handling, conditionals, loops, functions, strings, lists, dictionaries, and logical operations.

## Lab 1: The Smart Survey Onboarding Engine

This Python program building an entry portal for an automated processing system. The script must interview a human user, gather their basic profile info, and evaluate their clearance tier based on strict age rules.


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
## Input

```text
Enter your name: Alice
Enter your age: 25
Are you a developer? (yes/no): yes
```

## Expected Output

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


* input() capturing and Type Casting (int)
* Working with Boolean values
* Conditionals (if-elif-else) and Logic Operators (and, or)
* String Interpolation (f-strings)

---

## Lab 2: The Multi-Cluster IP Audit Tool


The Multi-Cluster IP Audit Tool is a Python program that analyzes a cloud cluster configuration and calculates infrastructure utilization. 

---


## Features

* Reads data from a nested dictionary structure
* Counts active nodes using a loop
* Calculates cluster utilization percentage
* Displays a formatted infrastructure report

---

## Function Specification

```python
def calculate_capacity(config):
```

### Config parameter

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

## Lab 3: The Deployment Budget Optimizer



The Deployment Budget Optimizer is a Python program that dynamically figures out the total monthly operational cost of setting up server groups and raises flags if things get too expensive. 

---


## Features

* Accepts deployment parameters dynamically
* Calculates monthly cloud infrastructure costs
* Compares expenses against a budget limit
* Returns informative approval or rejection messages

---

## Function Specification

```python
def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
```

### Parameters

| Parameter      | Type  | Description                    |
| -------------- | ----- | ------------------------------ |
| instance_count | int   | Number of server instances     |
| hourly_rate    | float | Hourly cost per instance       |
| budget_cap     | float | Maximum allowed monthly budget |

---

## Cost Calculation Formula

A standard billing month is assumed to contain:

```text
30 Days × 24 Hours = 720 Hours
```

Monthly Cost Formula:

```text
Total Monthly Cost = Instance Count × Hourly Rate × 720
```

---

## Business Rules

### If Cost Exceeds Budget

```text
REJECTED: Budget Exceeded by $X!
```

Where:

```text
X = Total Cost - Budget Cap
```

### If Cost Is Within Budget

```text
APPROVED: Total Estimated Cost is $X.
```

Where:

```text
X = Total Monthly Cost
```

---

## Example Test Cases

```python
print(estimate_deployment_cost(
    instance_count=5,
    hourly_rate=0.45,
    budget_cap=1500.00
))

print(estimate_deployment_cost(
    instance_count=12,
    hourly_rate=0.85,
    budget_cap=5000.00
))
```

---

## Expected Output

```text
REJECTED: Budget Exceeded by $120.00!
REJECTED: Budget Exceeded by $2344.00!
```

---

## Learning Objectives

* Functions with ParametersFunctions with Parameters and Return values
* Arithmetic Operations
* Comparative conditions (> ,<=)
* Calculated cost against the budget_cap:

---

# Lab 4: The Profile Text Normalization Pipeline

The Profile Text Normalization Pipeline is a Python program that clean text array before passing it downstream into production environments.

---


## Features

* Processes multiple text records automatically
* Removes leading and trailing whitespace
* Converts text to lowercase
* Stores cleaned data in a separate list
* Displays both original and sanitized results for comparison

---

## Raw Data

```python id="x9m7tw"
raw_survey_inputs = [
    "  ALICE SMITH ",
    " dhaka, BANGLADESH  ",
    "  mLOpS_ENGineer  ",
    "  LIAM,MAYA "
]
```

---

## Data Cleaning Process

Each record undergoes the following transformations:

### Step 1: Remove Extra Spaces

```python id="i3q7am"
text.strip()
```

### Step 2: Convert to Lowercase

```python id="39a8e1"
text.lower()
```

### Step 3: Store in Sanitized List

```python id="v32kw8"
sanitized_records.append(cleaned_text)
```

---

## Expected Output

```text id="khnffg"
Raw Input:
['  ALICE SMITH ', ' dhaka, BANGLADESH  ', '  mLOpS_ENGineer  ', '  LIAM,MAYA ']

Sanitized Production Input:
['alice smith', 'dhaka, bangladesh', 'mlops_engineer', 'liam,maya']
```

---

## Learning Objectives

* Work with Strings and String Methods(.strip(), .lower())
* Use `.strip()` to remove whitespace
* Use `.lower()` to standardize text
* Lists and Loops
* Appending dynamic modifications to lists

---

## Lab 5: System Alert Flag Evaluator


The System Alert Flag Evaluator is a Python program that simulates a basic infrastructure monitoring system. It  developing an automated error monitoring daemon. It continuously looks at a series of active machine flags to evaluate whether an urgent maintenance engineer needs to be page-alerted out of bed.

---


## Features

* Evaluates multiple monitoring conditions
* Uses compound boolean expressions
* Simulates production alerting logic
* Generates clear operational status messages

---

## Three telemetry boolean flags

```python
is_active = True
cpu_percent = 94.5
is_production = True
```

## Alert Rules

An alert should be triggered if **either** of the following conditions is true:

### Rule 1: Server Offline

```python
not is_active
```

The server is not running and requires immediate attention.

### Rule 2: Critical CPU Usage

```python
cpu_percent > 90.0 and is_production
```

CPU utilization exceeds 90% while operating in a production environment.

---

## Compound Alert Logic

```python
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)
```

---


## Example Evaluation

### Input 1

```python
is_active = True
cpu_percent = 94.5
is_production = True
```

### Expected Output

```text
[ALERT] Urgent dispatch! System needs manual intervention.
```

### Input 2

```python
is_active = True
cpu_percent = 74.5
is_production = True
```

### Expected Output

```text
[OK] System operating within safe margin bounds.
```


## Learning Objectives

* Complex boolean evaluations (and, not, or)
* Logical comparisons and flag validation
* Control execution states

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
python3 lab1_SmartSurvey.py
python3 lab2_ClusterAudit.py
python3 lab3_BudgetOptimizer.py
python3 lab4_TextNormalization.py
python3 lab5_AlertFlagEvaluator.py
```

---

## Technologies Used

* Python 3.14.6

## Author

**Name:** Sumona Salma

**Course:** Python Programming Fundamentals


