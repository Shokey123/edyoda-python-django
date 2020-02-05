#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import array as arr
a = arr.array('i',[1,2,3,4,5])
while True:
    print("1. Print Array")
    print("2. Add Element")
    print("3. Delete Element")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("The Array Elements are: ")
        for numbers in a:
            print(numbers)
    elif choice == 2:
        val = int(input("Please enter the integer number: "))
        a.append(val)
    elif choice == 3:
        value = a.pop()
        print("The Deleted value was: ",value)
    elif choice == 4:
        break
    else:
        print("Enter a valid choice")


# In[ ]:




