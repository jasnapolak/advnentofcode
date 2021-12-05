with open("data_3.txt", "r") as data:
    binary_data = data.read().split()


# PART 1
gamma_rate = ""
epsilon_rate = ""


for x in range(0, len(binary_data[0])):
    zero = 0
    one = 0

    for y in range(0, len(binary_data)):
        if binary_data[y][x] == '0':
            zero += 1
        else:
            one += 1

    if zero > one:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'


g = int(gamma_rate, 2)
e = int(epsilon_rate, 2)

print(g * e)


# PART 2
data2 = binary_data.copy()

index = 0

while len(binary_data) > 1:
    one = 0
    zero = 0
    ones_o2 = []
    zeroes_o2 = []

    for number in range(0, len(binary_data)):
        if binary_data[number][index] == '0':
            zero += 1
            zeroes_o2.append(binary_data[number])
        else:
            one += 1
            ones_o2.append(binary_data[number])

    if zero > one:
        binary_data = zeroes_o2
    else:
        binary_data = ones_o2
    index += 1

oxygen = binary_data
oxygen_generator_rating = int(binary_data[0], 2)
print(oxygen)
print(oxygen_generator_rating)

 # ...
binary_data = data2
index = 0

while len(binary_data) > 1:
    one = 0
    zero = 0
    ones_co2 = []
    zeroes_co2 = []

    for number in range(0, len(binary_data)):
        if binary_data[number][index] == '0':
            zero += 1
            zeroes_co2.append(binary_data[number])
        else:
            one += 1
            ones_co2.append(binary_data[number])

    if zero > one:
        binary_data = ones_co2
    else:
        binary_data = zeroes_co2
    index += 1

co2 = binary_data
co2_scrubber_rating = int(binary_data[0], 2)
print(co2)
print(co2_scrubber_rating)

print(co2_scrubber_rating * oxygen_generator_rating)
