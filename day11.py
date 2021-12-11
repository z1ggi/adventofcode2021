grid = []
counter = 0
sim = None
def flash(row, col, flashed):
  if grid[row][col] > 9 and (row, col) not in flashed:
    grid[row][col] = 0
    flashed.append((row, col))
    for r in range(max(row-1, 0), min(row+1, len(grid)-1)+1):
      for c in range(max(col-1, 0), min(col+1, len(grid[0])-1)+1):
        if (r,c) not in flashed:
          grid[r][c] += 1
          flash(r,c, flashed)


with open('./day11.txt', 'r') as file:
  for line in file:
    grid.append([int(n) for n in line.strip('\n') ])

  step = 1
  while not sim:
  # for step in range(100):
    flashed = []
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        grid[row][col] += 1
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        flash(row, col, flashed)
    counter += len(flashed)
    if len(flashed) == len(grid) * len(grid[0]):
      sim = step
    step += 1
# print(counter)
print(sim)