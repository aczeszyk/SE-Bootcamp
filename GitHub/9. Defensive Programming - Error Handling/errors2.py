# Corrected code below:

animal = "lion" # Syntax error: missing "" around lion. Changed to lower case l.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # Logical error: animal type and number of teeth in the wrong order.

print(full_spec) # Running error: missing brackets around variable.