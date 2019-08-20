
def fizzbuzz(number):
    fizz = number % 3 == 0
    buzz = number % 5 == 0

    if fizz and buzz : return "FIZZBUZZ"
    if fizz : return "FIZZ"
    if buzz : return "BUZZ"

    return number

if __name__ == "__main__":
    for i in range(20):
        print(fizzbuzz(i+1))