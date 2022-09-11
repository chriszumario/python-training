# Immutability of strings
fact = 'The Moon has no atmosphere.'
fact + 'No sound can be heard on the Moon.'
two_facts = fact + 'No sound can be heard on the Moon.'
print(two_facts)

# Multiline text
# multiline = '''Facts about the Moon:
# ...  There is no atmosphere.
# ...  There is no sound.'''
multiline = 'Facts about the Moon:\n There is no atmosphere.\n There is no sound.'
print(multiline)

# String methods in Python
heading = 'temperatures and facts about the moon'
print(heading.title())
# Split a string
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures .split())
# Search for a string
print('Moon' in 'This text will describe facts about the Moon')
temperatures = '''Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius.'''
print(temperatures.find('Saturn'))
# Check content
temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print(parts)


# Transform text
text = 'Temperatures on the Moon can vary wildly.'
print('temperatures' in text.lower())


# Percent sign (%) formatting
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' %
      mass_percentage)

# The format() method
print('''You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth'''.format('Moon', mass_percentage))

# About f-strings
print(
    f'On the Moon, you would weigh about {mass_percentage} of your weight on Earth')
