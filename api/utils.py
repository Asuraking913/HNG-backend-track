def handle_prime(number):
    if number < 2:
        return False
    else:
        if number % 2 != 0 and number % 3 != 0:
            return True
        else:
            return False

def handle_perfect(number):
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
    individual_nums = []
    
    if len(str(number)) <= 1:
        return number
    else:
        for num in str(number):
            if int(num) != 0 and int(num) < number:
                individual_nums.append(int(num))
        return sum(individual_nums)