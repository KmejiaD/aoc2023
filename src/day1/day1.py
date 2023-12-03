import re
def readFile():
    lines = []
    with open("input.txt") as file_in:
        for line in file_in:
            lines.append(line.rstrip('\n'))
    return lines

def part1():
    lines = readFile()
    total = 0
    for line in lines:
        for char in line:
            if char.isnumeric() :
                total += int(char)*10
                break
        for char in reversed(line):
            if char.isnumeric() :
                total += int(char)
                break
    print('solution Part 1: ', total)

def part2():
    numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    numbersR = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9,
               '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    regex = '(\d|one|two|three|four|five|six|seven|eight|nine)'
    regexReverse = '(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)'
    lines = readFile()
    total = 0
    for line in lines:
        match = re.search(regex, line).group()
        match2 = re.search(regexReverse,line[::-1]).group()
        total += numbers.get(match) * 10
        total += numbersR.get(match2)
    print('solution Part 2', total)


part1()
part2()
