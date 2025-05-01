from math import sqrt
prime = True

num = int(input("Enter a number to check if prime: "))

if num < 2:
    print("Not prime")
else:
    prime = True
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            prime = False
    if prime is True:
        print("Prime")
    else:
        print("Not prime")

