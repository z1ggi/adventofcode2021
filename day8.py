import re

def findMissingChar(s1, s2):
  r = ''
  for x in s1:
    if s2.find(x) == -1:
      r += x
  return r

def translate(line):
  r = {}
  for num in line:
    if len(num) == 2:
      r[1] = num
    elif len(num) == 4:
      r[4] = num
    elif len(num) == 3:
      r[7] = num
    elif len(num) == 7:
      r[8] = num

  # find segments c (in all but 5 and 6)
  fiveSix = None
  for ch in r[1]:
    found = list(filter(lambda num: not re.search(ch, num), line))
    if len(found) == 2:
      fiveSix = found
      break
  # find 5 and 6  
  r[5] = fiveSix[0] if len(fiveSix[0]) == 5 else fiveSix[1]
  r[6] = fiveSix[0] if len(fiveSix[0]) == 6 else fiveSix[1]

  # find segment e (in 6, not in 5)
  e = findMissingChar(r[6], r[5])
  # find 9 (8 - e)
  for num in line:
    if "".join(sorted(set(r[8].replace(e, '')))) == "".join(sorted(set(num))):
      r[9] = num
      break
  
  # reduce list
  for value in r.values():
    line.remove(value)
  # find 0, since it is the last number with 6 segments
  for num in line:
    if len(num) == 6:
      r[0] = num
      line.remove(num)
      break
  # find last 2 and 3. only 2 has segment e
  r[2] = line[0] if re.search(e, line[0]) else line[1]
  r[3] = line[1] if re.search(e, line[0]) else line[0]

  for key, value in r.items():
    r[key] = "".join(sorted(set(value)))
  return r

def calculate(line, output):
  resultStr = ''
  for o in output:
    o = "".join(sorted(set(o)))
    for key, value in line.items():
      if o == value:
        resultStr += str(key)
        break
  # print(int(resultStr))
  return int(resultStr)

with open('./day8.txt', 'r') as file:
  input = [line.strip('\n').split(' | ') for line in file]
  c = 0
  for line in input:
    newLine = translate(line[0].split())
    c += calculate(newLine, line[1].split())
  print(c)