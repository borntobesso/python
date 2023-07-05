kata = (19,42,21)

def display_numbers(numbers):
    num_count = len(numbers)
    numbers_str = ', '.join(str(number) for number in numbers)
    print(f'The {num_count} numbers are: {numbers_str}')

display_numbers(kata)