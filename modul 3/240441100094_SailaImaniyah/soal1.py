size= int (input("masukkan size: "))

#angka0
print('')
print ('n'*size)
for x in range (size-1):
    print('x',' '*(size-4),'x')
print('n'*size)

#angka9
print('')
rumus=size//3
print('i'*size)
for x in range (rumus):
    print('x',' '*(size-4),'x')
print('a'*size)
for b in range (rumus):
    print(' '*(size-2),'b')
print('c'*size)

#angka4
print('')
rumus=size//2
for x in range (rumus):
    print('x',' '*(size-4),'x')
print('a'*size)
for b in range (rumus):
    print(' '*(size-2),'b')