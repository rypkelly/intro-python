# check to find element in list

list1 = ['me', 'to', 'be', 'go', 'fo']
if 'me' in list1:
    print('here')

list1.append('fooo')
print(list1)

list1.insert(1, 'max')
print(list1)
list1.remove('to')
print(list1)
# delete works w index not value

del list1[3]
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)
i = list1.index('be')
print(i)

print(sorted(list1))
print(list1)

# immutable - you can't add or mess with
# tuple - remains in the same state for the entire code

tup1 = ('hello', 'hi', 'hey')
tup2 = (1, 2, 3)
tup3 = tup1 + tup2
list = [1,2,4]
tup = tuple(list)
print(tup3)
print(tup1[0:2])
print(len(tup3))
print(max(tup3))
print(min(tup3))

# string

# split()

# split(delim)
s = '2017,may,7,cs'
print(s.split(","))

# .lower()
s = 'StRiNG'
print(s.lower())
print(s)

# sub in string
x = 'Hello world'
print('hello' in x)






import random

# string

#split()

#split(delim)
s = '2017,may,7,cs'
print(s.split(","))

#.lower()
s = 'StRiNG'
print(s.lower())
print(s)

a = 'Hello'
b = ' Wo/r/ld/'
print(a + b)

#strip

print(b.strip('/')) #only on ends
print(b)
#find
print(a.find('o'))

print(b.replace('/', ''))


#dict
#no indexes
#use key:value pairs

dictionary = {'test': 'hi', 'test2': 'hello', 'david': 'seb'}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary['test'])

dictionary['test'] = 'marwan'
print(dictionary)

#--------------------------------------------------------------
list2 = [0,1,2,3,4,5,6]
random.shuffle(list2)
print(list2)
   #returns value
for i in range(0,5):
    x = random.randrange(0, len(list2)) #returns value
    print(list2[x])

#--------------------------------------------------------------
#reading files and loops
list2 = ['hi', 'hey', 'hello']
for i in range(len(list2)):
    print(i)   #print indices
    #print(list2[i]) #print elements

for i in list2:
    print(i)  #prints elements

for i in range(len(list2)):
    #list2[i] = 5
    pass

k=0
while(list2[k] != 'hey'):
    print(k)
    k+=1

#files
#read from url or one in a folder on computer
import urllib.request
file = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/snark.txt')
file2 = open('snark.txt', 'r').read().strip().split()



#whole_file = file.read()#read all at once
#whole_file_decoded = whole_file.decode('utf-8')
#print(whole_file_decoded)

for line in file:
    decoded = line.decode('utf-8').strip()
    list1 = decoded.split()

    #print(list1[0])

for i in range(0,5,2):
    print(i)

i = 0
while i<5:
    print(i)
    i += 1