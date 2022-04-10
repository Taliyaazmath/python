#implementing the list data structure methods

the_list=['hello', 5 ,'world',4 ,2022,5]
the_other_list=['good','night','everyone']

the_list.append('tuesday')
print(the_list)


y = the_list.copy()
print(y)

x= the_list.count(5)
print(x)

the_list.extend(the_other_list)
print(the_list)

z = the_list.index(5)
print(z)

t=the_list.insert(2,'the')
print(the_list)

the_list.pop(5)
print(the_list)

the_list.remove('world')
print(the_list)

the_list.reverse()
print(the_list)

the_other_list.sort()
print(the_other_list)

print(len(the_list))

the_list.clear()
print(the_list)


