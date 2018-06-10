from random import randint
from math import gcd

def provavel_primo(n, tentativas=20):
    if n < 1:
        return False
    
    while tentativas > 0:
        a = randint(2, 1000)

        while gcd(n, a) != 1:
            a = randint(2, 1000)
            
        if pow(a, n - 1, n) != 1:
            return False
        
        tentativas -= 1
    
    return True
