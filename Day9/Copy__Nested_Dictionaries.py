# Nested Dictionaries

student = {
    "1st" : {
        "name" : "Niket"
    },
    "2nd" :{
        "name" : "Kruparth"
    },
    "3rd" : {
        "name" : "Dhurv"
    }
}
print(student)

# 2nd way 

first = {
    "name" : "Niket"
}
second = {
    "name" : "Kruparth"
}
third = {
    "name" : "Dhurv"
}

student = {
    "first" : first,
    "second" : second,
    "third" : third
}
print(student)

# Loop Through Nested Dictionaries

student = {
    "1st" : {
        "name" : "Niket"
    },
    "2nd" :{
        "name" : "Kruparth"
    },
    "3rd" : {
        "name" : "Dhurv"
    }
}

for x , y in student.items():
    print(x)
    for z in y :
        print ( z + " : ", y[z])

# Access Items in Nested Dictionaries

student = {
    "1st" : {
        "name" : "Niket"
    },
    "2nd" :{
        "name" : "Kruparth"
    },
    "3rd" : {
        "name" : "Dhurv"
    }
}

print(student [ "2nd"] ["name"])