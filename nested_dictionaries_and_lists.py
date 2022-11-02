'''
Update Values in Dictionaries and Lists

Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
'''
from multiprocessing.sharedctypes import Value


x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory['soccer'][0] = "Andres"
print(sports_directory['soccer'])

z[0]["y"] = 30
print(z)

'''
Iterate Through a List of Dictionaries
Create a function iterate Dictionary (some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
'''
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    print(str(list[0])[1:-1:1])
    print(str(list[1])[1:-1:1])
    print(str(list[2])[1:-1:1])
    print(str(list[3])[1:-1:1])
iterateDictionary(students) 
'''
should output: (it's okay if each key-value pair ends up on 2 separate lines;
bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

'''
Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name
, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output:
'''
def iterateDictionary2(key_name, list):
    for i in range(0,len(list)):
        for key, value in list[i].items():
            if key == key_name:
                print(value)
iterateDictionary2('first_name', students)

'''
Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary
whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
'''
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(list):
    for i in range(0, len('locations')):
        locations = 0 + i
    print("------------")
    print(str(locations) + " " , "Locations")
    print(list['locations'][0])
    print(list['locations'][1])
    print(list['locations'][2])
    print(list['locations'][3])
    print(list['locations'][4])
    print(list['locations'][5])
    print(list['locations'][6])
    print("------------")
    for l in range(0, 9,):
        instructors = 0 + l
    print(str(instructors) + " " , "INSTRUCTORS")
    print(list['instructors'][0])
    print(list['instructors'][1])
    print(list['instructors'][2])
    print(list['instructors'][3])
    print(list['instructors'][4])
    print(list['instructors'][5])
    print(list['instructors'][6])
    print(list['instructors'][7])
printInfo(dojo)
# output:
'''
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''
