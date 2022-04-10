the_dict={'apples':20,'orange':10,'mango':15,'pineapple':5,'kiwi':8}
x1=('hello','good')
y1=('world','night')

print("1",len(the_dict))

x=the_dict.copy()
print("2",x)

dic=dict.fromkeys(x1,y1)
print(dic)

y = the_dict.get('apples')
print("3",y)

z = the_dict.items()
t = dic.items()
print("4",z)
print("4",t)

z1 = the_dict.keys()
print("5",z1)

dic.pop('good')
print("6",dic)

the_dict.popitem()
print("7",the_dict)

t1 = the_dict.setdefault('apples',30)
print("8",t1)

the_dict.update({"banana":13,"watermelon":3})
print("9",the_dict)

l = the_dict.values()
r = dic.values()
print(l)
print(r)

dic.clear()
print(dic)




