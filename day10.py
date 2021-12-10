m = {
  '(': ')',
  '[': ']',
  '<': '>',
  '{': '}'
}
c = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}
cc = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}
with open('./day10.txt', 'r') as file:
  errorCh = []
  corrections = []  
  for line in file:
    b = []
    withError = False
    for ch in line.strip('\n'):
      if ch in m.keys():
        b.append(ch)
      elif len(b) and ch == m[b[-1]]:
        b.pop()
      elif len(b) == 0:
        break
      else:
        errorCh.append(ch)
        withError = True
        break
    if len(b) and not withError:
      r = ''
      for ch in b:
        r = m[ch] + r
      corrections.append(r)

  res = 0
  for x in errorCh:
    res += c[x]
  print(res)

  points = []
  for cor in corrections:
    p = 0
    for x in cor:
      p = p*5 + cc[x]
    points.append(p)
  points.sort()
  print(points[int(len(points)/2)])