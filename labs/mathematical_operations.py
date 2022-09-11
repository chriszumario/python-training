# Addition
from math import ceil, floor
answer = 30 + 12
print(answer)  # Output: 42

# Subtraction
difference = 30 - 12
print(difference)  # Output: 18

# Multiplication
product = 30 * 12
print(product)  # Output: 360

# Division
quotient = 30 / 12
print(quotient)  # Output: 2.5

# Work with division
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22


# Exercise - Display distance between planets
first_planet = 9879879
second_planet = 6876834587
distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

# Convert strings to numbers
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

# Output:
# 215
# 215.3


# Absolute values
print(abs(39 - 16))
print(abs(16 - 39))

# Output
# 23
# 23

# Rounding
print(round(14.5))

# Output: 15

# Math library

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12

#  Convert strings to numbers and use absolute values
first_planet_input = int(
    input('Enter the distance from the sun for the first planet in KM: '))
second_planet_input = int(
    input('Enter the distance from the sun for the second planet in KM: '))
distance_km = second_planet_input - first_planet_input
print(abs(distance_km))
