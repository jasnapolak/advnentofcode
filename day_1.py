
with open("data_1.txt", "r") as depth_measurements:
    measurement = depth_measurements.read().split()

depth_increased = 0

prev = measurement[0]
for num in measurement[1:]:
    if int(num) > int(prev):
        depth_increased += 1
    prev = num

print(depth_increased)
