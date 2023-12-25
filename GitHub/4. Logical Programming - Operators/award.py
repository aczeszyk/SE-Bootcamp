#read swimming time (in minutes)
#read cycling time (in minutes)
#read running time (in minutes)
#calculate total time taken to complete triathlon
#display total time (in minutes)
#determine which award a person qualifies on based on the total time
#if total time less than or equal to 100, person receives provicial colours
#if total time between 101-105, person receives provicial half colours
#if total time between 106-110, person receives provicial scroll
#if total time greater than 111, person receives no award
#display message with which award a person receives

swim_time = int(input("What is you swimming time? (in minutes) "))
cycle_time = int(input("What is you cycling time? (in minutes) "))
run_time = int(input("What is you running time? (in minutes) "))
total_time = swim_time + cycle_time + run_time
print(f"Your total race time is {total_time} minutes.")

if total_time <= 100:
    print("Congratulations! Your race time qualifies for a Provincial Colours Award.")
elif total_time > 100 and total_time <= 105:
    print("Very good job! Your race time qualifies for a Provincial Half Colours Award.")
elif total_time >105 and total_time <= 110:
    print("Well done! Your race time qualifies for a Provincial Scroll Award.")
elif total_time >= 111:
    print("Sorry, your race time does not qualify for an award. Good luck next time.")