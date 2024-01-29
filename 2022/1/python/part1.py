# Advent of Code - 2022 - Day 1 - Part 1

def main():
    with open('../input.txt') as f:
        lines = f.readlines()
        blocks = ''.join(lines).split('\n\n')
        blocks = [block.replace('\n', ' ') for block in blocks]
        total_sums = []
        biggest = 0

        for block in blocks:
            sum = 0
            if block == '':
                continue
            block = block.split(' ')
            for i in range(block.__len__()):
                sum += int(block[i])
            total_sums.append(sum)

        for i in range(total_sums.__len__()):
            if total_sums[i] > biggest:
                biggest = total_sums[i]

        print("Sum of most calories: " + biggest.__str__())


if __name__ == '__main__':
    main()
