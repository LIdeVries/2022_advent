with open("Day6.txt") as myfile:
    signal = myfile.readline()

score = 4
while True:
    window = set(signal[score - 4 : score])
    if len(window) == 4:
        print(score)
        break
    score += 1
