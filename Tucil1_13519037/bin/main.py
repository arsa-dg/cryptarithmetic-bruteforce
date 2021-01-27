import time

#list tiap line pada file
def readFile(filename):
  stringList = []
  with open(filename,'r') as file:
    for line in file:
      stringList.append(line.strip('\n'))

  return stringList

#mencari list character yang ada
def charList(filename):
  stringnya = ''
  with open(filename,'r') as file:
    for line in file:
      stringnya += line.strip(' \n+-')
  return list(set(stringnya))

#mencari kemungkinan-kemungkinan pasangan
def genPermutasi(theList, size, n, hasil):
  if (size == 1):
    tampung = []
    for i in range(n):
      tampung = tampung + [theList[i]]
    hasil.append(tampung)

  for i in range(size):
    genPermutasi(theList, size-1, n, hasil)

    if (size%2 == 1):
      tmp = theList[0]
      theList[0] = theList[size-1]
      theList[size-1] = tmp
    else:
      tmp = theList[i]
      theList[i] = theList[size-1]
      theList[size-1] = tmp

#checker pasangan sesuai atau tidak
def checker(theList):
  jumlah = 0
  for i in range(len(theList)-2):
    jumlah += theList[i]

  if (jumlah == theList[len(theList)-1]):
    return True
  else:
    return False

#main program
file = input("Masukkan nama file yang terletak di folder /test/ (contoh: 1.txt) : ")
direktori = 'test/'+file

try:
  open(direktori)
except:
  direktori = '../test/'+file
try:
  open(direktori)
except:
  direktori = 'Tucil1_13519037/test/'+file

initList = readFile(direktori)
Chara = charList(direktori)

initTime = time.perf_counter()

permutasi = []
genPermutasi([0,1,2,3,4,5,6,7,8,9], 10, len(Chara), permutasi)
counter = 0

for perm in permutasi:
  counter += 1
  convList = []

  #pasangan angka dan huruf
  pair = []
  for i in range(len(Chara)):
    pair.append([Chara[i],perm[i]])

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
  
  #pasangan sesuai ketemu
  if (not(isFZero) and checker(convList)):
    for line in initList:
      print(line.rjust(9))

    print()
    for lineConv in range(len(convList)):
      if (lineConv == len(convList)-3):
        print(('+ ' + str(convList[lineConv])).rjust(9))
      else:
        print(str(convList[lineConv]).rjust(9))
    print('Waktu eksekusi program', time.perf_counter()-initTime, 'detik')
    print('Jumlah total tes', counter, 'kali')
    break
else:
  print('Tidak ada solusi yang memenuhi')