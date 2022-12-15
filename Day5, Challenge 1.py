import pandas as pd

"""figure out how to change the list inplace"""

# Creating list of Stacks
# This is the stacks original, cleaning and sorting.
with open("Day5.txt") as myfile:
    stacks = myfile.readlines()[0:8]
    saved = []
for line in stacks:
    line = line.replace("\n", "")
    line = line.replace("    ", " ")
    item = line.split(" ")
    saved.append(item)

# Reversing Stacks and clearing out blanks
stacks = []
restacked = zip(*saved)
restacked = list(restacked)

for number in range(len(restacked)):
    restacked[number] = list(restacked[number])
    restacked[number].reverse()
    restacked[number] = [x for x in restacked[number] if x != ""]


# Creating DataFrame commands.
# This captures the origin of the boxes, the destination, and the count of boxes to be moved
commands = pd.read_csv("Day5.txt", skiprows=8)

# Cleaning Commands DF
commands.columns = ["command"]
commands = commands.pop("command").str.extractall("(\d+)")[0].unstack().astype(int)
commands.columns = ["count", "origin", "destination"]

print(commands)
for item in restacked:
    print(item)
print("then")
for index, row in commands.iterrows():
    for iterations in range(row["count"]):
        moving = restacked[row["origin"] - 1].pop()
        restacked[row["destination"] - 1].append(moving)


output = ""
for item in restacked:
    output += item[-1][1]
print(output)
