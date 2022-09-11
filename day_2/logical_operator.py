# OR
temperature = 95
if temperature > 80 or temperature < 60:
    print('Stay inside!')
else:
    print('Enjoy the outdoors!')

# AND
forecast = 'rain'
if temperature < 80 and forecast != 'rain':
    print('Go outside!')
else:
    print('Stay inside!')

# NOT
if not forecast == 'rain':
    print('Go outside!')
else:
    print('Stay inside!')
