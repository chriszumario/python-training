# Create a list
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Access list items by index
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

# Output
# The first planet is Mercury
# The second planet is Venus
# The third planet is Earth

# Determine the length of a list
number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

# Output:
# There are 8 planets in the solar system


# Add values to lists
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

# Output:
# There are actually 9 planets in the solar system.

# Remove values from lists
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets,
      'planets in the solar system.')


# Use negative indexes
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus


# Find a value in a list
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

# Output
# Jupiter is the 5 planet from the sun

#  Work with numbers in lists
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650  # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs',
      bus_weight * gravity_on_planets[0], 'kg')

# Output
# On Earth, a double-decker bus weighs 12650 kg
# On Mercury, a double-decker bus weighs 4781.7 kg

# Use min() and max() with lists
bus_weight = 12650  # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is',
      bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is',
      bus_weight * max(gravity_on_planets), 'kg')

# Output
# On Earth, a double-decker bus weighs 12650 kg
# The lightest a bus would be in the solar system is 4769.05 kg
# The heaviest a bus would be in the solar system is 29854 kg

# Manipulate list data
# Slice lists
planets = ['Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']

# Join lists
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

# Sort lists
regular_satellite_moons.sort()
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']
