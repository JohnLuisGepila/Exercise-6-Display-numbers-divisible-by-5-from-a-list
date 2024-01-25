def display_numbers_divisible_by_five(numbers):
    for number in numbers:
        if number % 5 == 0:
            print(number)

numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
display_numbers_divisible_by_five(numbers)
