from typing import ItemsView


def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n
    
    print("Sum: ", sum)

adder(5,4)
adder(5,2,7)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(fname="Sneh", lname="Kandoi",Age=20,Phone=6446546546)


# add ,update,clear,del,remove,pop,convert list into set,convert dictonary into set,union,intersection,issuperset,difference,simetric difference,isdisjoint,

list = ['items1,item2']
# list.add('items3')
print(list)

demo = set()
demo.add("sneh")
list.update(demo)
print(list)

list1 = ['item1','items2']
list1.clear()
print(list1)

list2 = ['i1','i2','i3']
del list2

list3 = ['i1','i2','i3','i4','i5']
list3.remove('i2')
print(list3)

list3.pop()
print(list3)

list4 = [1,2,3,4,5,6]
myset = set(list4)
print(myset)

dict = {'a':1,'b':2,'c':3,'d':4}
item_set = set(dict.items())
print(item_set)


