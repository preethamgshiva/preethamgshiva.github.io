student_dict={
    'first_name':'John',
    'Last_name':'Doe',
    'Gender':'Male',
    'age':25,
    'marital-status':'Unmarrie',
    'skills':['bike-riding','Painting','Cooking'],
    'country':'India',
    'city':'Blore',
    'address':'RR nagar'
}

print(len(student_dict))

print(student_dict['skills'])
print(type(student_dict['skills']))

student_dict['skills'].append('Football')

keylist=list(student_dict.keys())
print(keylist)

valuelist=list(student_dict.values())
print(valuelist)

print(student_dict.items())
list_tuple=(keylist)
print(list_tuple)

del(student_dict['Gender'])
print(student_dict)

del(student_dict)
print(student_dict)