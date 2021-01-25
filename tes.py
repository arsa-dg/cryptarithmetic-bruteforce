import time
#kurang permutasi

def readFile(filename):
  stringList = []
  with open(filename,'r') as file:
    for line in file:
      stringList.append(line.strip('\n'))

  return stringList

def wordList(filename):
  stringnya = ''
  with open(filename,'r') as file:
    for line in file:
      stringnya += line.strip(' \n+-')
  return list(set(stringnya))

def permutasinya(iterable, r=None):
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = list(range(n))
  cycles = list(range(n, n-r, -1))
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i+1:] + indices[i:i+1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return

def checker(theList):
  jumlah = 0
  for i in range(len(theList)-2):
    jumlah += theList[i]

  if (jumlah == theList[len(theList)-1]):
    return True
  else:
    return False

initList = readFile('testing.txt')
Chara = wordList('testing.txt')
# print(Chara)

initTime = time.perf_counter()

#permutasi sementara
permutasi = list(permutasinya([1,2,3,4,5,6,7,8,9,0], len(Chara)))
counter = 0

for perm in permutasi:
  counter += 1
  convList = []

  #pasangan angka dan huruf
  pair = []
  for i in range(len(Chara)):
    pair.append([Chara[i],perm[i]])
  # print(pair) 

  for line in initList:
    angka = 0
    lineCleaned = line.strip(' \n+-')
    for c in lineCleaned:
      isFZero = False
      for cari in range(len(pair)):
        if (c == pair[cari][0]):
          if (c == lineCleaned[0] and pair[cari][1] == 0):
            isFZero = True
          break
      if(isFZero):
        break
      angka = angka*10 + pair[cari][1]
    
    if(isFZero):
      break
    if ('-' in line):
      convList.append(line)
    else:
      convList.append(angka)
  # print(convList)
  
  if (not(isFZero) and checker(convList)):
    for line in initList:
      print(line)

    for lineConv in range(len(convList)):
      if (lineConv == len(convList)-3):
        print(convList[lineConv], '+')
      else:
        print(convList[lineConv])
    print('Waktu eksekusi program', time.perf_counter()-initTime)
    print('Jumlah total tes', counter)
    break
else:
  print('Tidak ada solusi yang memenuhi')