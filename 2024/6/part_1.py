current_pos = []
rotations = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
direction = "^"
moves = {'^': [-1, 0], 'v': [1, 0], '<': [0, -1], '>': [0, 1]}
visited = set()

with open('input.txt', 'r') as file:
    matrix = [list(line.strip()) for line in file]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if "^" in matrix[y][x]:
                current_pos = [y, x]

    visited.add((current_pos[0], current_pos[1]))

    while True:
        next_pos = [current_pos[0] + moves[direction][0], current_pos[1] + moves[direction][1]]
        if not (0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix[0])):
            break
        if matrix[next_pos[0]][next_pos[1]] == '#':
            direction = rotations[str(direction)]
            continue
        current_pos = next_pos
        visited.add((current_pos[0], current_pos[1]))

print(len(visited))
