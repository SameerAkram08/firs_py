def number(limit):
    a=0
    b=1
    
    while a <= limit:
        yield a
        a, b = b, a + b

limit = int (input("Enter the limit of required Fibonacci series = "))
fib_generator = number(limit)

for num in number(limit):
    print(num)

