def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_recursive (n, i = 2):
    if n<2: return False
    if n==2: return True
    if i==n: return True
    if n%i==0: return False
    return is_prime(n, i+1)

        
print(is_prime(1))  #> False
print(is_prime(2))  #> True
print(is_prime(3))  #> True
print(is_prime(5))  #> True
print(is_prime(9))  #> False
print(is_prime(15)) #> False