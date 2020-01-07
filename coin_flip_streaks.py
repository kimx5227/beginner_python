import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    HorTlist = []
    for i in range(100):
        if random.randint(0,1) == 1:
            HorTlist.append('H')
        else:
            HorTlist.append('T')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 0
    oldflip = HorTlist[0]
    for i in HorTlist:
        if i == oldflip:
            count +=1
            if count == 6:
                numberOfStreaks += 1
                break
        else:
            count = 0
            oldflip = i

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
