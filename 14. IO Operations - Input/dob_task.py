# Open the text file and read in each line as a string.

dob_file = open('DOB.txt', 'r+')

with open('DOB.txt', 'r+') as dob_file:
    dob_data = dob_file.readlines()

# Create an empty list for names and birthdates variable.
# Split each line into each word as a separate string.
# Per line, store the first 2 strings as names and the rest as birthdates.

names = []
birthdates = []

for line in dob_data:
    words = line.split()
    names.append(words[:2])
    birthdates.append(words[2:])

# Print all names as one list. (Two values in a tuple: name, surname).
    
print("\033[1m Name \033[0m") 
for name, surname in list(names):
    print(name, "".join(surname))
print("\n")

# Print all birthdates as one list. (Three values in a tuple: day, month, year).

print("\033[1m Birthdate \033[0m")
for day, month, year in list(birthdates):
    print(day, month, "".join(year))
