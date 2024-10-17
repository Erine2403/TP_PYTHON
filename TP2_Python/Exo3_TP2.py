import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO)

def fizz_buzz(n):
    n = int(n)
    
    if n % 3 == 0 and n % 5 == 0:
        logging.info(f"{n} est divisible par 3 et 5")
        return "fizz buzz"
    elif n % 3 == 0:
        logging.info(f"{n} est divisible par 3")
        return "fizz"
    elif n % 5 == 0:
        logging.info(f"{n} est divisible par 5")
        return "buzz"
    else:
        logging.info(f"{n} n'est divisible ni par 3 ni par 5")
        return "le nombre donné en paramètre n'est pas divisible par 3 et 5"
