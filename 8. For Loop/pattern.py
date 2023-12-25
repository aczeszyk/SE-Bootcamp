# Star pattern, which increases with the number of rows and then decreases, using an if-else statement within a for loop.

rows = 5
for i in range(1, 2 * rows):
    if i <= rows:
        stars = i
        print("*" * stars)
    else:
         stars = (2 * rows) - i
         print("*" * stars)

