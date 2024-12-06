#Dictionary
# dict = {
#     "name" : 'zara',
#     'age': 7,
#     'class' : 'first'
# }

# dict['age']= 8
# dict['class']= "two" 
# dict['sekolah']= 'UTM'
# del dict['name']
# dict.clear()
# data_copy = dict.copy()

# print(data_copy)
# print(data_copy.get('name'))
# print('name' in data_copy)
# print('alamat' in data_copy)
# print(data_copy.keys())
# data_copy.pop('age')

# print(data_copy)
# print("dict['name']",dict['name'] )
# print("dict['age']",dict['age'])
# print("dict['class']",dict['class'])
# print("dict['sekolah']",dict['sekolah'])
# print(f"{dict}")


#Himpunan
#contoh set
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

#menambahkan elemen ke set menggunakan add()
set_b.add(9)
print(set_b)

# set_a.union(set_b)
#set_a.intersection(set_b)
himpunan = set_a.difference(set_b)
print (himpunan)


#Contoh cara membuat dictionary pada python
# dict = {'name':'Zara', 'Age':7,'Class': 'First'}
# print ("dict['Name']", dict['Name'])
# print ("dict['Age']", dict['Age'])


#Update dictionary python
dict = {'Name': 'Zara', 'Age':7, 'Class':'First'}
del dict['Name'] #hapus entri dengan key 'Name'
dict.clear()    #hapus semua entri di dict
del dict        #hapus dictionary yang sudah ada


print ("dict['Age']:", dict['Age'])
print ("dict['School']:", dict['School'])
