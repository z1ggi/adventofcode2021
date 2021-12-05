pipes = []
grid = []

def compareTo(a,b):
  if a > b:
    return 1
  elif a < b:
    return -1
  else:
    return 0

with open('./day5.txt', 'r') as file:
  maxX = 0
  maxY = 0
  for line in file:
    (l, r) = list(map(lambda x: list(map(lambda y: int(y), x.split(','))), line.strip('\n').split(' -> ')))
    # print('{} -> {}'.format(l, r))
    maxX = max(maxX, l[0], r[0])
    maxY = max(maxY, l[1], r[1])
    pipes.append([l, r])
  grid = [[0] * (maxX + 1) for i in range(maxY + 1)]

  for pipe in pipes:
    (l, r) = pipe
    xDirection = compareTo(r[0], l[0])
    yDirection = compareTo(r[1], l[1])

    # part one
    # if l[0] == r[0] or l[1] == r[1]:
    position = [l[0], l[1]]
    while position != r:
      grid[position[1]][position[0]] += 1
      position[0] += xDirection
      position[1] += yDirection
    grid[position[1]][position[0]] += 1

# for i in grid:
#   print(i)
flatGrid = [i for line in grid for i in line]
print('count: {}'.format(len(list(filter(lambda x: x > 1, flatGrid)))))