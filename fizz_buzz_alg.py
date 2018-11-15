def fizz_buzz(input):
    if input % 3==0 and input % 5==0:
        return "fizzbuzz"
    if input % 3==0:
        return "fizz"
    if input % 5==0:
        return "buzz"


fb = fizz_buzz(5)
print(fb)
