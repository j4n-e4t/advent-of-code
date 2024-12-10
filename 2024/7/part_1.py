operators = ["+", "*"]
total_calibration = 0

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        result = eval(f"{result} {op} {numbers[i + 1]}")
    return result

with open("input.txt") as file:
    for line in file:
        line = line.strip().split(":")
        res, calc = int(line[0]), [int(x) for x in line[1].strip().split(" ")]
        found_solution = False
        combinations = []
        stack = [[]]

        while stack:
            current = stack.pop()
            if len(current) == len(calc) - 1:
                combinations.append(current)
                continue

            for op in operators:
                stack.append(current + [op])

        for ops in combinations:
            if evaluate_expression(calc, ops) == res:
                found_solution = True
                break

        total_calibration += res if found_solution else 0

print(total_calibration)
