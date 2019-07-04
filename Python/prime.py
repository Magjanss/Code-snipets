#Generate primes


primes = [2]

def checkprime(number):
    for prime in primes:
        if number % prime == 0 :
            return False
    primes.append(number)
    return True
    

if __name__ == "__main__":
    i = 3
    while True:
        checkprime(i)
        i+=1
        if i > 300000 : break
    print(primes)

