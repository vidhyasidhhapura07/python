# Loop Through a Dictionary 

    # showing only keys 

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat",
 }

for  v in student:
    print(v)


    #  showing only value

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat",
 }

for v in student:
    print(student[v])   
    
# keys() method

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat",
}

for v in student.keys():
    print(v)

 
 # values() method

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat",
 }

for v in student.values():
    print(v)

#  items() method

student = {
    "name" : "Niket",
    "age" : 25,
    "city" : "surat",
 }

for v , n in student.items():
    print(v  , n)


for v , n in student.items():
    print(v + " : " , n)