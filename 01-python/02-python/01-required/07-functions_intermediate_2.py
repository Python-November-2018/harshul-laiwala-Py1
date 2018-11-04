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

# How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  
x[1][1]=10
print(x)
# How would you change the last_name of the first student from 'Jordan' to "Bryant"?
for i in range(len(students)):
    if students[i]['last_name'] == 'Jordan':
        students[i]['last_name'] = 'Bryant'
        print(students[i])
# For the sports_directory, how would you change 'Messi' to 'Andres'?
for i in range(len(sports_directory['soccer'])):
    if sports_directory['soccer'][i] =='Messi':
        sports_directory['soccer'][i]='Andres'
print(sports_directory)


# For z, how would you change the value 20 to 30?
for i in range(len(z)):
    if z[i]['y'] == 20:
        z[i]['y'] =30
    print(z)