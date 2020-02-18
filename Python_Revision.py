#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Mutable datatypes:
    list
    dict
    set
Immutable:
    int
    float
    tuple
    str


# In[ ]:


Mutable :change at same memory location
Immutable : change at same memory location is not possible


# In[ ]:


id() => Memory location


# In[ ]:


type() => data type


# In[5]:


l1 = [10,20,30]
l2 = [10,20,30]
print(id(l1))       #Id or memory location will be different
print(id(l2))


# In[ ]:


num1 = 1000
num2 = 1000


# In[ ]:


object intering


# In[ ]:


start with alpha
_
FIRST_NUM => constants
first_name  firstName(Not like this)


# In[ ]:


== : => compare values (comparision Operator)
is : => compares memory location (Identity Operator)


# In[ ]:


num1 = 10
print(num1%2 == 5)


# In[ ]:


(/, =>, floor, div)


# In[ ]:


get_ipython().run_line_magic('=>', 'remainder')


# In[ ]:


(=>, perfect, division)


# In[ ]:


True/False:
    identity is is not
    membership in not in
    logical and or not
    comparison == != < >  <= >=


# In[ ]:


str  => char
list  => elements
tuple  => elements
set    => elements
dict  => keys
fp : line  \n


# In[ ]:


print(5 in d) => here d should be iterable from above


# In[ ]:


non zero => True
Zero " " [] () {} => False None


# In[11]:


l = [10,20,30,40,50]
for i in enumerate(l):    #==> enumerate gives indexing and value and output data in tuple
    print(i)
    
    
    #OR
    
l = [10,20,30,40,50]
for index,value in enumerate(l):
    print(index,value)


# In[12]:


x = 100,200
print(type(x))  #if more then two values are by default Tuple


# In[14]:


x,y = 100,200
print(type(x))


# In[16]:


num1, num2 = 100,200
num1, num2 = num2, num1   #=> Swap two values
print(num1,num2)


# In[ ]:


for x in 100:
    print(x)   #=> x should be iterable datatype


# In[ ]:


for user_var in [iterable datatype]:
    print(user_var)
else:
    print("after completing it will come here")


# In[ ]:


while (condition):
    statements
else:
    print("after completing that it comes here")


# In[ ]:


str:
    count
    len
    
    split
    join
    
    replace
    upper
    lower
    title
    
    isupper
    islower
    istitle
    
    isalpha
    isalnum
    isdigit
    
    find
    count
    index
    
    center
    ljust
    rjust
    
    strip
    lstrip
    rstrip
    
    format
    
    
    


# In[ ]:


print(dir(str))  #To see built in functions


# In[ ]:


help(str)   #To read Documentation


# In[ ]:


help(str.find)  #help someting special


# In[ ]:


split str=> list, 
join => list => str (" ").join(l)


# In[26]:


s = "Python Java C"
l = (",").join(s)
print(l)


# In[28]:


num1 = 100
num2 = 200

s = "{n1} {n2}".format(n2=num1, n1=num2)
print(s)


# In[ ]:


isalnum "a 999 bdlg"


# In[31]:


#ASCII value
print(ord('a'))
print(chr(97))


# In[ ]:


start
end
stride  => 1  => left to right index left to right


# In[37]:


s = "Hello! how are you"   
#print(s[1:6:-1])          #Invalid slice so it prints nothing
print(s[5:-1])


# In[38]:


s = "hello! how are you"
print(s[2])


# In[ ]:


List :
    add:
        append   => one element
        extend   => Multiple element
        insert   => index,value
        
    update:
        l[index] = new_vale
        
    Delete:
        pop      =>    index last
        remove  => value first
        clear   => empty list
        del    =>  del ref


# In[39]:


l = [10,20,30,40,50, [100,200,300]]
print(l[-1][1])                        #Reaching to particular element


# In[40]:


l = [100,200,300,400,500,600]
for value in l[1:-1]:
    print(value)


# In[41]:


l1 = [10,20,30]
l2 = l1
#l2 = l1.copy()
print(id(l1), id(l2))


# In[43]:


l = [10,20,30,40]
#print(tuple(l))    #changing list into tuple
print(str(l))       #changing list into str


# In[ ]:


dict:
    mutable => add, update and delete
    unordered => not support indexing and slicing
    keys should be unique
    keys should be immutable


# In[46]:


d = {1:1,2:2,3:3,4:4}
d[5] = 5
d.setdefault(6,6)  #if key exists then it will not update new key and value
print(d)        #if key doesn't exists then it will update new key and value


# In[ ]:


keys()
values()
items()  => key,val


# In[50]:


l1 = [1,2,3]
l2 = [1,4,9]
d = dict(zip(l1,l2))   #changing list into dictionary as key and value
print(d)


# In[51]:


l = [10,20,30,40]
print(set(l))


# In[52]:


d = {1:1,2:4}
print(set(d))  #when dict is converted to set then it gives keys only


# In[53]:


d = set()
print(type(d))


# In[ ]:


sets :
    mutable
    unordered
    element should be unique
    all the elements should be immutable


# In[ ]:


union  => only unique elements from both the sets
intersection => common elements from both the sets
s1 difference s2  => when elements from s1  are not in s2 or different
symmetric diff => all elements from s1 and s2 except common element

issubset  =>  if all the elements are present in each other or not
issuperset  => 



# In[ ]:


dict del:
    popitem  => will arbitrarily select and remove, it returns key and value
    pop    => only return value which is removed
    clear

    del


# In[ ]:


sets:
    discard(40)
    remove(40)


# In[56]:


print("Python "* 2)


# In[ ]:


def func_name(args):
    pass

func_name(10,20)


# In[ ]:


parameter passing techniques:
    1. Positional 
    2. Default     def num=100
    3. keyword     =>  values will be passed using keywords
    
    def login(username,password)
    
    login(password = "abc", username = "abc@123")
    
    4. Var positional    *args => tuple
    5. Variable keyword  **kwargs => dict


# In[ ]:


def add(num1 = 10, num2, num3, **kwargs, *args) #it will not run because all should be in sequence


# In[ ]:


sequence of arguments:
    positional
    default
    var positional
    var keyword


# In[ ]:


import => max upto module level => pkg1.pkg2.mod
pkg1.pkg2.mod.add(10,20)


# In[ ]:


from pkg1.pkg2 import mod
mod.add(10,20)


# In[ ]:


fp = open("filename","mode")


# In[ ]:


tag :initial :operation :if file doesn't exist
r, start, read, error
r+ => start, read + write , error

w  => start, write, create
w+ => start, write + read, create file

a  => end of the file, write at the end, create
a+ => end of the file, write at the end, create


# In[ ]:


r+
w+


# In[ ]:


seek(offset,position)
0: start of the file
1: current position
2: end of the file
    
    seek(100,0)


# In[ ]:


regx :
    . it will match with single or any single char
     [a-z]+
     [0-9]*
      get_ipython().run_line_magic('pinfo', '')
      ^ => start of the
      $ => end of the
      [^a-z] => other than a-z
      ^[a-z] => match with a-z
        
        \w [a-zA-Z0-9]   #compliment to each-other
        \w [^a-zA-Z0-9]
        
        \s #space
        \S #anything other than space
        
        \d => digits
        \D => #anythin other than digits
    


# In[58]:


import re


# In[ ]:


re.compile
re.findall(r,s) =>  #all the occurrence of r in s
re.search(r,s) => #first occurrence => match.group(0)


# In[61]:


r = re.compile("([0-9]{2})-([0-9]{2})-([0-9]{4})")
s = "12-12-2019"
m = re.search(r,s)
print(m.group(0))


# In[63]:


r = re.compile("(?P<day>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})")
s = "12-12-2019"
m = re.search(r,s)
print(m.group("day"))


# In[ ]:


COMPREHENSION:


# In[65]:


l = [10,20,30,40,50]
l2 = [value * value for value in l]
print(l2)


# In[69]:


l = [10,20,30,40,50]
l2 = [value * value for value in l if value % 3 == 0]
print(l2)


# In[ ]:


map
filter


# In[ ]:


map  => built in function which takes fuc as an argument
map(func,iterable)


# In[72]:


def add(num1,num2):
    return num1 + num2
l1 = [1,2,3]
l2 = [100,200,300,400]
print(list(map(add,l1,l2)))


# In[76]:


def add(num1,num2):
    return num1 + num2
l1 = [1,2,3]
l2 = [100,200,300,400]
print(tuple(map(lambda num1,num2: num1 + num2,l1,l2)))


# In[79]:


l = [10,25,30,35,40,45,100]
l2 = [value for value in l if value%2 ==0]
print(l2)


# In[82]:


l = [10,25,30,35,40,45,100]
f = filter(lambda num1: num1 % 2 == 0,l)
print(list(f))


# In[ ]:




