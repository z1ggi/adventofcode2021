import os

# power consumption
a = None
gamma = ''
epsilon = ''
lineNumber = 0

with open('./day3.txt', 'r') as file:
  for line in file:
    lineNumber += 1
    if a is None:
      a = [0] * (len(line) - 1)
    for i in range(len(line) - 1):
      a[i] += int(line[i])

for i in range(len(a)):
  gamma += str(int(a[i] > lineNumber / 2))
  epsilon += str(int(a[i] < lineNumber / 2))
print('gamma {}, in dez: {}'.format(gamma, int(gamma, 2)))
print('epsilon {}, in dez: {}'.format(epsilon, int(epsilon, 2)))
print('power consumption: {}'.format(int(gamma, 2) * int(epsilon, 2)))

# life support rating
ogr = []
co2sr = []

def findRating(arr, most = True, i = 0):
  if len(arr[0]) < i:
    raise Exception('i to long')
  if 1 == len(arr):
    return arr[0]
  ones = []
  zeros = []
  for line in arr:
    if '1' == line[i]:
      ones.append(line)
    else:
      zeros.append(line)
  if most:
    arr = ones if len(ones) >= len(zeros) else zeros
  else:
    arr = ones if len(ones) < len(zeros) else zeros

  return findRating(arr, most, i + 1)


with open('./day3.txt', 'r') as file:
  for line in file:
    line = line.strip('\n')
    ogr.append(line)
    co2sr.append(line)

ogr = findRating(ogr, True)
co2sr = findRating(co2sr, False)
print('oxygen generator rating: {}'.format(ogr))
print('CO2 scrubber rating'.format(co2sr))
print('life support rating: {}'.format(int(ogr,2) * int(co2sr, 2)))