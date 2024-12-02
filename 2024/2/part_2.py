def is_safe_sequence(numbers):
    if len(numbers) < 2:
        return True
    increasing = None
    for i in range(len(numbers)-1):
        diff = numbers[i+1] - numbers[i]
        if diff == 0:
            return False
        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            return False
        if abs(diff) > 3:
            return False
    return True

def check_with_dampener(numbers):
    if is_safe_sequence(numbers):
        return True
    for i in range(len(numbers)):
        dampened = numbers[:i] + numbers[i+1:]
        if is_safe_sequence(dampened):
            return True
    return False

safe_count = 0
with open("input.txt", "r") as file:
    for line in file:
        numbers = [int(x) for x in line.strip().split()]
        if check_with_dampener(numbers):
            safe_count += 1

print(safe_count)
