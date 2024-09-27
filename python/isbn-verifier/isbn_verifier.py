def is_valid(isbn):
    multiplier = 10
    sum = 0
    numbers = []
    
    for idx, char in enumerate(isbn):
        if char.isdigit():
            numbers += [int(char)]
        if char == 'X' and idx == 12:
            numbers += [10]
        if char == '-':
            continue
        else:
            continue
            
    if len(numbers) is not 10:
        return False
        
    for idx, number in enumerate(numbers):
        sum += number * (10 - idx)
        
    return sum % 11 == 0
