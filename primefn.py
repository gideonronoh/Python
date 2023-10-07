num = range (1,1000)
def is_prime (num):
  for X in range (2,num):
    if num %X == 0:
        return False
    return True

primes = list (filter(is_prime, num))
print(primes)
