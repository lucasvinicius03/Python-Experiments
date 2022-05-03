from functools import reduce

def lcm(*integers):
    integers = list(integers)
    current_divisor = 2
    multiples = []
    while True:
        divide = True
        while divide:
            divide = False
            for i, x in enumerate(integers):
                if (x % current_divisor == 0): 
                    integers[i] = x / current_divisor
                    divide = True
            if divide == True: multiples.append(current_divisor)
        current_divisor += 1
        if all(num==1 for num in integers): break
    return reduce((lambda a, b: a * b), multiples)

def next_prime(number):
    while True:
        divisors = 0
        number += 1
        for div in range(2, number):
            if number % div == 0: divisors += 1
        if divisors == 0: return number

if __name__ == '__main__':
    import cProfile, random
    
    test_numbers = tuple(random.randint(1,1001) for x in range(10))
    cProfile.run('lcm(*test_numbers)')

