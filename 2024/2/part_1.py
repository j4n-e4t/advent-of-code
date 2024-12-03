safe_report_count = 0

def check_all_numbers_increase_or_decrease(numbers):
    original_numbers = numbers.copy()
    return original_numbers == sorted(numbers) or original_numbers == sorted(numbers, reverse=True)

def check_max_difference(numbers):
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i-1])
        if diff < 1 or diff > 3:
            return False
    return True

with open("input.txt", "r") as file:
    for line in file:
        numbers = [int(x) for x in line.strip().split()]
        if check_all_numbers_increase_or_decrease(numbers) and check_max_difference(numbers):
            safe_report_count += 1

print(safe_report_count)
