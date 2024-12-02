safe_report_count = 0

def check_all_numbers_increase_or_decrease(numbers):
    increasing = None
    for i in range(len(numbers)-1):
        diff = numbers[i+1] - numbers[i]
        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            return False
    return True

def check_max_difference(numbers):
    for i in range(len(numbers)-1):
        diff = abs(numbers[i+1] - numbers[i])
        if diff < 1 or diff > 3:
            return False
    return True

with open("input.txt", "r") as file:
    for line in file:
        numbers = [int(x) for x in line.strip().split()]
        if check_all_numbers_increase_or_decrease(numbers) and check_max_difference(numbers):
            safe_report_count += 1

print(safe_report_count)
