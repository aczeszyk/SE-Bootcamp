# Code to calculate a user's holiday cost based on the
# plane cost, hotel cost, and car rental cost.

# Print out options of destinations

def flight_options():
    print("______________________________\n")
    print("Destination Options:\n")
    print("1. Barcelona (£100)")
    print("2. Prague (£65)")
    print("3. Mexico (£1000)")
    print("4. Quit")
    print("______________________________\n")

flight_options()

# User inputs the required information:
# 1. City they are flying to.
# 2. Number of nights they will be staying.
# 3. Number of days they will be renting a car.

import sys

while True:
    city_flight = input("Please select which city you would like to go to: ")
    if city_flight in ["1", "2", "3"]:
        break
    elif city_flight == "4":
        sys.exit("You chose to quit. Goodbye!")
    else:
        print("\033[31mSorry, select a number from the menu.\033[0m")


while True:
    num_nights = input("How many nights you will be staying at the hotel: ")
    if num_nights.isnumeric():
        break
    else:
        print("\033[31mPlease enter a number.\033[0m")
    

while True:
    rental_days = input("How many days you will be hiring a car for: ")
    if rental_days.isnumeric():
        break
    else:
        print("\033[31mPlease enter a number.\033[0m")


# Creating functions that will calculate the cost of
# hotel, flights, car rental, and total holiday cost.
        
def hotel_cost():
    total = 50 * int(num_nights)
    return total

def plane_cost():
    if city_flight == "1":
        cost = 100
        return cost
    elif city_flight == "2":
        cost = 65
        return cost
    elif city_flight == "3":
        cost = 1000
        return cost    

def car_cost():
    total = 35 * int(rental_days)
    return total

def holiday_cost():
    total = plane_cost() + hotel_cost() + car_cost()
    return total

# Output of all costs.
print("\n______________________________\n")
print(f"The total cost for your hotel is: \033[33m£{hotel_cost()}\033[0m.")
print("\n______________________________\n")

print(f"Your total flight cost is: \033[33m£{plane_cost()}\033[0m.")
print("\n______________________________\n")

print(f"The total cost for your car rental is: \033[33m£{car_cost()}\033[0m.")
print("\n______________________________\n")

print(f"Your total holiday cost is: \033[33m£ {holiday_cost()}\033[0m.")
print("\n______________________________\n")