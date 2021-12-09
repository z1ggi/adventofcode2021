m = []
def check(row, col, checked):
  checked.append([row, col])
  cur = m[row][col]
  #up
  if row > 0 and [row-1, col] not in checked:
    if cur > m[row-1][col]:
      return None
    elif cur == m[row-1][col]:
      return check(row-1, col, checked)
  #left
  if col > 0 and [row, col-1] not in checked:
    if cur > m[row][col-1]:
      return None
    elif cur == m[row][col-1]:
      return check(row, col-1, checked)
  #down
  if row < len(m)-1 and [row+1, col] not in checked:
    if cur > m[row+1][col]:
      return None
    elif cur == m[row+1][col]:
      return check(row+1, col, checked)
  #right
  if col < len(m[0])-1 and [row, col+1] not in checked:
    if cur > m[row][col+1]:
      return None
    elif cur == m[row][col+1]:
      return check(row, col+1, checked)
  return cur
  
def identifyBasin(row, col, checked):
  checked.append([row, col])
  cur = m[row][col]
  c = 1
  #up
  if row > 0 and [row-1, col] not in checked and m[row-1][col] != 9:
    c += identifyBasin(row-1, col, checked)
  #left
  if col > 0 and [row, col-1] not in checked and m[row][col-1] != 9:
    c += identifyBasin(row, col-1, checked)
  #down
  if row < len(m)-1 and [row+1, col] not in checked and m[row+1][col] != 9:
    c += identifyBasin(row+1, col, checked)
  #right
  if col < len(m[0])-1 and [row, col+1] not in checked and m[row][col+1] != 9:
    c += identifyBasin(row, col+1, checked)
  return c

with open('./day9.txt', 'r') as file:
  for line in file:
    m.append([int(x) for x in line.strip('\n')])
  lows = []
  basins = []
  for row in range(len(m)):
    for col in range(len(m[0])):
      x = check(row, col, [])
      if x is not None:
        lows.append(x+1)
        basins.append(identifyBasin(row, col, []))
r = 1
for i in range(3):
  r *= max(basins)
  basins.remove(max(basins))
print(sum(lows))
print(r)
