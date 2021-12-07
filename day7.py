with open('./day7.txt', 'r') as file:
  positions = [int(p) for p in file.readline().strip('\n').split(',')]
  leastPos = None
  for i in range(min(positions), max(positions)):
    steps = 0
    for p in positions:
      steps += sum(range(abs(p - i)+1))
    if leastPos is None or steps < leastPos[1]:
      leastPos = (i, steps)
  print(leastPos)