"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:

    result = 0

    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]  #numbers is a list
        sorted_numbers = sorted(numbers)
        
        if len(sorted_numbers)%2 == 0:
            result = ( sorted_numbers[len(sorted_numbers)//2 - 1] + sorted_numbers[len(sorted_numbers)//2] ) / 2  #list count from zero
        else:
            result = ( sorted_numbers[len(sorted_numbers)//2])

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
    
        
print(result)