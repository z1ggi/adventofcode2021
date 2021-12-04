increases = 0
with open('./day1.txt', 'r') as file:
  prev = file.readline()
  for line in file:
    if int(line) > int(prev):
      increases += 1
    prev = line
print('increases: {}'.format(increases))

increases = 0
with open('./day1.txt', 'r') as file:
  arr = []
  for line in file:
    line = int(line)
    if len(arr) < 4:
      arr.append(line)
      # print('{}'.format(arr))
    if len(arr) == 4:
      arr.pop(0)
      arr.append(line)
      increases += int(sum(arr)-arr[0] > sum(arr) - arr[3])
      # print('{} => {} vs {} = {}'.format(arr, sum(arr)-arr[3], sum(arr)-arr[0], int(sum(arr)-arr[0] > sum(arr) - arr[3])))
print('increases: {}'.format(increases))