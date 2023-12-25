# Ask user to enter a number repeatedly.
# If the number is -1, stop requesting number from user.
# Calculate average of the numbers, excluding -1.

numbers = []

while True:
  number = input("Please enter a number: ")
  if number == "-1":
    break
  else:
    numbers.append(float(number))
average = sum(numbers)/len(numbers)
print(f"The average of your numbers is {average}.")
