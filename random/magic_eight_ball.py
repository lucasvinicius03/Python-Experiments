import random
from itertools import cycle
from time import sleep
from os import system

def clear():
    system('cls||clear')

ball = (
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
)

loading = cycle(('▲', '►', '▼', '◄'))

while True:
    clear()
    if input('Would you like to ask the magic 8-ball? (y/n)? ').lower()[0] == 'n':
        break
    print('Think of a yes-no question')
    for x in range(random.randint(4, 10)):
        print('Thinking ' + next(loading), end='\r')
        sleep(0.5)
    print(ball[random.randint(0, len(ball)-1)])
    input()