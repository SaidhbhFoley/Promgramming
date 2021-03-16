# Programme that counts how many times it was run
# Author: Saidhbh

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
num = readNumber()
print (num)

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

num = readNumber()
num += 1
print ("We have run this program {} times".format(num))
writeNumber(num)