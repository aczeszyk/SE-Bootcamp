# Open a new file called student register
# and create a new text file called reg form in write mode.

student_register = open('reg_form.txt', 'w')

# User inputs the number of students they are registering.

student_number = int(input("How many students are you registering? "))

# For the number of students that are being registered,
# the user is asked to input their ID number.

for students in range(0, student_number):
    id_number = input("Enter student ID number: ")
    if id_number.isnumeric():
        student_register.write(id_number + " .................." + "\n")
    else:
        print("This is not a number.")

student_register.close()