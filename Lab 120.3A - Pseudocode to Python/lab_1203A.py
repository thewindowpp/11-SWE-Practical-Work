# Lab 120.3A - Pseudocode to Python

from p_num import process_number

count = 0
num = 0

while True:
    num = int(input("Please enter a number: "))

    if num >= 0:
        process_number(num)
        count += 1
    else:
        print("Negative number entered. Ending input.")
        break

    if num >= 0:
        print(f"Numbers processed: {count}")

