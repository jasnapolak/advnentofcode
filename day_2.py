with open("data_2.txt", "r") as commands:
    com = commands.read().splitlines()


horizont = 0
depth = 0

# PART 1
# for line in com:
#     line = line.split()
#     if line[0] == "forward":
#         horizont += int(line[1])
#     elif line[0] == "down":
#         depth += int(line[1])
#     else:
#         depth -= int(line[1])


# PART 2
aim = 0
for line in com:
    line = line.split()
    if line[0] == "forward":
        horizont += int(line[1])
        depth += aim * int(line[1])
    elif line[0] == "down":
        aim += int(line[1])
    else:
        aim -= int(line[1])

print(horizont * depth)
