def time_calculator(time, prettify = False):
    '''Can sum and subtract different time units.
    \nTo use it pass an equation following the 'valueunitoperation' pattern to the time_calculator() function.
    \nIt will return a tuple containing (Y, D, H, M, S)
    \nOptionally you can pass True to the param prettify. Doing so will change the output to ('YyDdMmHhSs', 'DdMmHhSs', 'MmHhSs', 'HhSs', 'Ss')
    \nValid units (y: year, d: day, h: hour, m: minute, s: second), valid operations (+: sum, -: difference)
    \ne.g. 12d+43s-45m-2h; 4y; 5m+3h; 2s...'''

    units = [x for x in time if x in 'ydhms']
    operations = [x for x in time  if x in '+-']
    values = time
    for char in '+-':
        values = values.replace(char, ' ')
    for char in 'ydhms':
        values = values.replace(char, '')
    values = [int(x) for x in values.split(' ')]

    seconds = []
    for v, u in zip(values, units):
        if u == 's':
            seconds.append(v)
        elif u == 'm':
            seconds.append(v*60)
        elif u == 'h':
            seconds.append(v*3600)
        elif u == 'd':
            seconds.append(v*86400)
        elif u == 'y':
            seconds.append(v*31536000)

    total_seconds = seconds[0]
    for i, op in enumerate(operations):
        if op == '+':
            total_seconds += seconds[i+1]
        else:
            total_seconds -= seconds[i+1]

    years = total_seconds/31536000
    days = total_seconds/86400
    hours = total_seconds/3600
    minutes = total_seconds/60

    if prettify:
        s = f'{total_seconds%60}s'
        ms = f'{total_seconds%3600//60}m{s}'
        hms = f'{total_seconds%86400//3600}h{ms}'
        dhms = f'{total_seconds%31536000//86400}d{hms}'
        years = f'{int(years)}y{dhms}'
        days = f'{int(days)}d{hms}'
        hours = f'{int(hours)}h{ms}'
        minutes = f'{int(minutes)}m{s}'
        total_seconds = f'{total_seconds}s'

    return years, days, hours, minutes, total_seconds

if __name__ == '__main__':
    time = input('Enter an equation that follows the \'valueunitoperation\' pattern\n e.g. 12d+43s-45m-2h\n').lower()
    years, days, hours, minutes, total_seconds = time_calculator(time, True)
    print(f'\nThis is equal to ' + years + ' or ' + days + ' or ' + hours + ' or ' + minutes + ' or ' + str(total_seconds)+'s')