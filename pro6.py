mylist=[{'apples':20,'orange':10,'mango':15,'pineapple':5,'kiwi':8},
        {'apples':30,'orange':40,'mango':65,'pineapple':50,'kiwi':20},
        {'apples':50,'orange':12,'mango':70,'pineapple':60,'kiwi':30}]
for i in mylist:
    print (i['apples'],i['orange'],i['mango'],i['pineapple'],i['kiwi'])

mydic={'apples':20,'orange':10,'mango':15,'pineapple':5,'kiwi':8}

a=mydic.items()
print(a)

for key,val in mydic.items():
    print(val)
