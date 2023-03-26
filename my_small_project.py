import time

# Define the position of body 
first_position = "Arms in Position 1, legs together"

# Define the consequence of movements
movements = [
    "Step movement to the right",
    "Eshapo in place",
    "Pirouette to the right",
    "Step movement to the left",
    "Reverance"
]

# Reproduction of the movements
for movement in movements:
    print(movement)
    time.sleep(1)


#This code allows to reproduce the sequences of 
# movements for classical ballet with 'print' 
# and time delays by using the function.