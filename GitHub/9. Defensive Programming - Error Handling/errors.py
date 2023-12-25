# Corrected code below:

print("Welcome to the error programme") # Syntax error - print function was missing brackets.
print("\n") # Syntax error - incorrect indentation and again no brackets.

# Syntax error - lines 8 to 17 had incorrect indentation.

# Variables declaring the user's age, casting the str to an int, and printing the result

age_str = "24" # Logical error - could not convert string 'years old' to an integer. Runtime error - single = to declare a variable, not ==.
age = int(age_str)
print(f"I'm {age} years old.") # Logical error - needed spaces between 'I'm', age, and 'years old' as well as format function to output integer as a string.

# Variables declaring additional years and printing the total years of age

years_from_now = 3.5 # Logical error - changed from string to integer value. Added 0.5 to include 6 extra months mentioned in line 24.
total_years = age + years_from_now
print(f"The total number of years: {total_years}.") # Logical error - needed format function to print integer value as string. Syntax error - incorrect variable name as answer_years was not defined.

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = total_years * 12 # Syntax error - had incorrect variable as total was not defined.
total_months = int(total_months) # Logical error - changed value from float to integer so no decimal places in output.
print(f"In 3 years and 6 months, I'll be {total_months} months old.") # Logical error - needed format function to print integer value as string.