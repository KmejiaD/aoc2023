
class Game:
    id:0
    dices:[]
def readFile():
    games = []
    with open("input.txt") as file_in:
        for line in file_in:
            line = line.rstrip('\n')
            games.append(parseInput(line))
    return games

def parseInput(line):
    result = Game()
    result.dices = []
    lineColonSplit = line.split(':')
    gameId = lineColonSplit[0].replace('Game ', '')
    result.id = int(gameId)
    gamesSplit = lineColonSplit[1].split(';')
    for game in gamesSplit:
        dices = {}
        groups = game.split(',')
        for group in groups:
            split = group.strip().split(' ')
            if dices.__contains__(split[1]):
                dices.__setitem__(split[1],dices.get(split[1])+int(split[0]))
            else :
                dices.__setitem__(split[1],int(split[0]))
        result.dices.append(dices)
    return result

def part1():
    games = readFile()
    dices = {'red': 12, 'green': 13, 'blue': 14}
    total = 0
    for game in games:
        valid = True
        for key in dices.keys():
            for dice in game.dices:
                if dice.__contains__(key):
                    if dice.get(key) > dices.get(key):
                        valid = False
        if valid:
            total += game.id
    print(total)

part1()