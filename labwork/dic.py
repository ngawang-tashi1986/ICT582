myD = {'name':'Ngawang Tashi', 'id': 1234, 'grade': 'a'}  #{} is use to define a dictionary

myD = [{'name':'Ngawang Tashi', 'id': 1234, 'grade': 'a'},
       {'name':'Tashi', 'id': 124, 'grade': 'b'},
       {'name':'Ngawang', 'id': 234, 'grade': 'b'}]
print(myD['name'])

for a in myD:
    print(myD[a])

print(myD.values)

print(myD.keys)

for v in myD.values():
    print(v)

print(myD[1]['id'])

for i in range(0, len(myD)):
    print(myD[1]['id'])

for i in range(0, len(myD)):
    sum = sum + myD[i]['id']

print(myD[1]['id'])


#student = {'ID':st_id,'q2': f_q1, 'q2':f_q2}

#for dictionary in all_student:
#    print("Student ID :" , dictionary['ID'])
#    print("Grade :" , dictionary['grade'])

#for tm in all_student:
#    total_marks = total_marks + tm['final']



