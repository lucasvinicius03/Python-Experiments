# Python-Experiments
Some random experiments I'm making while learning how to use python's modules.

## Python (general python):
### time_calculator.py
Can sum and subtract different time units.  
To use it pass an equation following the 'valueunitoperation' pattern to the time_calculator() function.  
It will return a tuple containing (Y, D, H, M, S)  
Optionally you can pass True to the param prettify. Doing so will change the output to ('YyDdMmHhSs', 'DdMmHhSs', 'MmHhSs', 'HhSs', 'Ss')  
Valid units (y: year, d: day, h: hour, m: minute, s: second), valid operations (+: sum, -: difference)  
e.g. 12d+43s-45m-2h; 4y; 5m+3h; 2s...

## Turtle Module:
### turtle-shape-thingy.py
Draws a shape and continuously draws inside it with a configurable offset.

### happy_birthday.py
A simple python file that I made for a friend. It draws balloons on the screen and whishes them happy birthday. The best part is that it can fit in a QR Code so if your phone is has a python IDE it is able to run it 
#### IMPORTANT **(if you're going to run this on a phone make sure to: decrease the font size to 15, set the balloon position addition to 50 instead of 10, set the writer(text, pos) pos variable to (0,60) and (0,-60), set the sleep function to 0.1 instead of 0.03 and the t1.pensize() to 3)**

### gravity.py
A ball but with ***physics***. Probably not very accurate. I'm not a physicist.
