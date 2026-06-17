#1. TODO: Capture inputs from user (Name, Age, Developer Status)

# Capturing inputs (stores as a string)
name = input("Enter your name: ") 
age_input = input("Enter your  age: ") 
dev_status = input("Are you developer? (Yes/No): ").lower().strip() # Capturing input and lower().strip() converts the text to lowercase, removes whitespace 

#handle error
try:
    age = int(age_input) # Type casting to an integer
except ValueError:
    # Exit if the string cannot be converted
    print("Error: Enter valid age.")
    exit()

status_options = ["yes", "no"]
# Checking developer status valid or not
if dev_status not in status_options:
    print(f"Error: Enter valid developer status (Yes/No) .")

#2. TODO: Evaluate conditional logic to determine the clearance tier    
if age < 18:
    tier = "Tier 3: Guest"
elif age >= 18 and dev_status == "yes":
    tier = "Tier 1: Admin Infrastructure Access"
else:
    tier = "Tier 2: Standard Executive Access"


#3. TODO: Print out the final profile card using an f-string
print("\n" * 1)
print(f"""Final profile card...
- Name is: {name}
- Age is: {age}.
- Developer status is: {dev_status}.
- Clearance tier is: {tier}.""")

print("\n" * 1)



