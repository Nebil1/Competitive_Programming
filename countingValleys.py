def countingValleys(steps, path):
    seaLevel = 0
    valley = 0
    for i in path:
        if i == 'D':
            seaLevel -= 1
        else:
            seaLevel += 1
            if seaLevel == 0:
                valley += 1
    return valley