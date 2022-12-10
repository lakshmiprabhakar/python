d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print("Original dictionary : ",d)
list1=list(d.items())
 #convert the given dict. into list
list1.sort()               #sort the list
print("Ascending order is ",list1)
list1=list(d.items())
list1.sort(reverse=True)    #sort in reverse order
print("Descending order is ",list1)
dict=dict(list1) # convert the list in dictionary 
print("Dictionary ",dict)
