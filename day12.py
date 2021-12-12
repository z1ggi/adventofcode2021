paths = []
result = []

def findPath(cur, visited, result):
  if cur.islower():
    v = visited[:]
    v.append(cur)
    allLowers = list(filter(lambda x: x.islower(), v))
    dups = set([x for x in allLowers if allLowers.count(x) > 1])
    treeTimes = set([x for x in dups if v.count(x) > 2])
    if len(dups) > 1 or len(treeTimes):
      return
  visited.append(cur)
  # print('cur: {}, visited: {}'.format(cur, visited))
  if cur == 'end':
    result.append(visited)
    return
  for path in filter(lambda p: p[0] == cur, paths):
    findPath(path[1], visited[:], result)


with open('./day12.txt', 'r') as file:
  paths = [tuple(line.strip('\n').split('-')) for line in file]
  reversePaths = []
  for path in paths:
    if path[0] != 'start' and path[1] != 'end':
      reversePaths.append((path[1], path[0]))
  for path in filter(lambda x: x[1] == 'start' or x[0] == 'end', paths):
    paths.remove(path)
  paths.extend(reversePaths)

  found = findPath('start', [], result)
  # for path in filter(lambda p: p[0] == 'start', paths):
  #   print(path)
# for r in result:
#   print(r)
print(len(result))