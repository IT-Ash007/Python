list1 = ["Alpha", "Beta", "Charlie", "Delta", "Gamma",100]
print(list1)
print(list1[2],list1[5]) #list index startes from 0
list2 = [101,5,29,73,52,38]
list2.sort()
print(list2)
list2.reverse()
print(list2)
list2.append(97)
print(list2)
list2.insert(1,104)
list2.remove(29)
print(list2)
print(len(list2))
list2.pop() # removes last element
print(list2)
print(len(list2))
list2[5]=7 #lists are mutable but tuples are immutable
print(list2)
#tuples
tp1=(1, 2, 3) #this is a tuple not list
#tp1[1]=20 value cannot be chnaged
