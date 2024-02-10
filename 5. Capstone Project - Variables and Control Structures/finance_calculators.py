import math

# Print menu message and let user choose  calculation - bond or investment.
# If neither picked, print error message.

message = " Investment - to calculate the amount of interest you'll earn on your investment. \n Bond - to calculate the amount you'll pay on a home loan. \n \n Enter either 'investment' or 'bond' from the menu above to proceed: "
print(message)

while True:
    user_choice = input(" \n Please choose Bond or Investment: ")
    user_choice = user_choice.lower()

    if user_choice == "bond" or user_choice == "investment":
        print(" Thank you.")
        break
    else:
        print(" \n Sorry, that's not right. Please type Bond or Investment: ")

if user_choice  == "bond" or user_choice  == "investment":
    print(" Thank you.")
else:
    print(" Sorry, that's not right. Please type either Bond or Investment. ")
  
# If investment chosen:
# Ask user to input deposit value.
# Ask yser to input interest rate.
# Ask user to input number of years they plan on investing.
# Ask user to choose simple or compoud interest.
# Output the amount of money user will receive for either option.

if user_choice == "investment":
    deposit = float(input(" Please enter the amount of money you are depositing: "))
    interest_rate = float(input(" Please enter your interest rate (%): "))
    interest_rate = interest_rate / 100
    years = float(input(" Please enter the number of years you are planning on investing: "))
    interest = (input(" Please choose between simple or compound interest: "))
    interest = interest.lower()
    if interest == "simple":
        total_interest = (deposit *(1 + (interest_rate) * years))
        total_interest = round(total_interest, 2)
        print(f" Your total interest earned will be £{total_interest}.")
    elif interest =="compound":
        total_interest = (deposit * math.pow(1+(interest_rate), years))
        total_interest = round(total_interest, 2)
        print(f" Your total interest earned will be £{total_interest}.")

# If bond selected:
# Ask user to input current house value.
# Ask user to input interest rate.
# Ask user to input number of months they plan to take to repay the bond.
# Output how much money the user will have to pay each month.

if user_choice == "bond":
    house_value = float(input(" Please enter the current value of your house: "))
    rate_interest = float(input(" Please enter your interest rate (%): "))
    rate_interest = (rate_interest / 100) / 12
    time = float(input(" Please enter the number of months you plan to take to repay your bond: "))
    repayment = (rate_interest * house_value) / (1 - (1 + rate_interest)**(-time))
    repayment = round(repayment, 2)
    print(f" Your monthly repayments will be £{repayment}.")
