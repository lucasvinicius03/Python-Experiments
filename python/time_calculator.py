time = input('Enter an equation that follows the \'valueunitoperation\' pattern\n e.g. 12h+43s-45m-2h\n').lower()

values = time
for char in '+-':
    values = values.replace(char, ' ')
for char in 'hms':
    values = values.replace(char, '')

values = [int(x) for x in values.split(' ')]
units = [x for x in time if x in 'hms']
operations = [x for x in time  if x in '+-']

seconds = []
for v, u in zip(values, units):
    if u == 's':
        seconds.append(v)
    elif u == 'm':
        seconds.append(v*60)
    else:
        seconds.append(v*3600)

total_seconds = seconds[0]
for i, op in enumerate(operations):
    if op == '+':
        total_seconds += seconds[i+1]
    else:
        total_seconds -= seconds[i+1]

hours = f'{total_seconds//3600}h{total_seconds%3600//60}m{total_seconds%60}s'
minutes = f'{total_seconds//60}m{total_seconds%60}s'
print(f'\nThis is equal to ' + hours + ' or ' + minutes + ' or ' + str(total_seconds)+'s')