def main(number):
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 != 0:
        return number
    return "Fizz"