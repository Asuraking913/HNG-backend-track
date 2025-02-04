def handle_prime(number):

    if number < 0:
        return False

    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    # Check divisibility up to sqrt(number)
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6  # Skip even numbers
    
    return True


def handle_perfect(number):
    
    if number < 0:
        return number + 3

    list_divisors = []

    for numbers in range(number):
        if numbers != 0:
            if number % numbers == 0: 
                list_divisors.append(numbers)
    return sum(list_divisors)

def handle_properties(number):

    properties = []
    individual_nums = []

    # handle armstrong
    # Split individual digits
    if int(number) > 0:
        for num in str(number):
            if int(num) != 0 and int(num) < number:
                individual_nums.append(num)
    
    new_nums = [int(num) ** len(str(number)) for num in individual_nums]
    new_nums = sum(new_nums)

    if new_nums == number:
        properties.append('armstrong')
    
    # handle even or odd
    if number % 2 == 0:
        properties.append('even')
    else:
        properties.append('odd')

    return properties

def handle_sum(number):

    number = abs(number)
    individual_nums = []
    
    if len(str(abs(number))) <= 1:
        return number
    else:
        for num in str(number):
            if int(num) != 0 and int(num) < number:
                individual_nums.append(int(num))
        return sum(individual_nums)