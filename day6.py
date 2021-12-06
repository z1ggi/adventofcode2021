with open('./day6.txt', 'r') as file:
  fish = file.readline().strip('\n').split(',')
  fish = {
    0: fish.count('0'),
    1: fish.count('1'),
    2: fish.count('2'),
    3: fish.count('3'),
    4: fish.count('4'),
    5: fish.count('5'),
    6: fish.count('6'),
    7: fish.count('7'),
    8: fish.count('8')
  }
  for i in range(256):
    fish = {
      0: fish[1],
      1: fish[2],
      2: fish[3],
      3: fish[4],
      4: fish[5],
      5: fish[6],
      6: fish[7] + fish[0],
      7: fish[8],
      8: fish[0]
    }
print(sum(fish.values()))