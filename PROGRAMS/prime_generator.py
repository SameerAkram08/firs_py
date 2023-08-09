def is_prime(n):
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

prime_gen = prime_generator()

X = input ("Enter range = ")

for _ in range(int(X)):
    print(next(prime_gen))
