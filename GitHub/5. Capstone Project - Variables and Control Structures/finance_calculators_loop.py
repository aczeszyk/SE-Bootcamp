import math

# Print message and let user choose  calculation - bond or investment

message = " Investment - to calculate the amount of interest you'll earn on your investment. \n Bond - to calculate the amount you'll pay on a home loan. \n \n Enter either 'investment' or 'bond' from the menu above to proceed: "
print(message)


while True:
    calculation = input(" \n Please choose Bond or Investment: ")
    calculation = calculation.lower()

    if calculation == "bond" or calculation == "investment":
        print(" Thank you.")
        break
    else:
        print(" \n Sorry, that's not right. Please type Bond or Investment: ")
    
 
# If investment chosen, output the amount of money user will receive

if calculation == "investment":
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

# If bond, calculate how much money the user will have to pay each month (insert formula here)

if calculation == "bond":
    house_value = float(input(" Please enter the current value of your house: "))
    rate_interest = float(input(" Please enter your interest rate (%): "))
    rate_interest = rate_interest / 100
    time = float(input(" Please enter the number of months you plan to take to repay your bond: "))
    repayment = (rate_interest * house_value) / (1 - (1 + (rate_interest / 12))**(-time))
    repayment = round(repayment, 2)
    print(f" Your monthly repayments will be £{repayment}.")
    