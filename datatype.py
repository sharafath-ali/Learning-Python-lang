from platform import java_ver
from typing import Type

#list
a=[1,'helo',3]
print(a[1])
print(type(a))
#tuple
a=(1,'helo',5)
print(a[0])
print(type(a))
#string
name="jima"
print(name)
print(type(name))
print(name[1])
print(len(name))
#dictionary
ed={'a':1,'b':22}
print(ed['b'])
print(type(ed))
#int
s=1
print(type(s))
#ffloat
u=9.6
print(type(u))
#multiline
g='eee'\
    'samsam'\
'd'
print(g)
print(type(g))
#string concetation
s='fu'
print(s+ g)
print(str(2))
#scanf
print("Where do you live?")
location = input()
print("So you live in " + location)