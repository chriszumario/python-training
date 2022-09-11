# Write if statements
a = 93
b = 27
if a >= b:
    print(a)

# Work with else
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

# Work with elif
a = 93
b = 27
if a >= b:
    print('a is greater than or equal to b')
elif a == b:
    print('a is equal to b')

# Work with nested conditional logic
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print('a is greater than b and b is greater than c')
    else:
        print('a is greater than b and less than c')
elif a == b:
    print('a is equal to b')
else:
    print('a is less than b')


# The or operator
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

# The and operator
a = 23
b = 34
if a == 34 and b == 34:
    print(a + b)
