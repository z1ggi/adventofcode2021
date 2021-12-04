pos = 0
depth = 0
aim = 0
with open('./day2.txt', 'r') as file:
  for line in file:
    line = line.split(' ')
    key = line[0]
    value = int(line[1])
    if key == 'forward':
      pos += value
      depth += aim * value
    elif key == 'down':
      aim += value
    else:
      aim -= value
      # depth = 0 if depth < 0 else depth
print(pos*depth)