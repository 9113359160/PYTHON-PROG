Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input("enter a value")
enter a value
>>> b =input("enter b value")
enter b value
>>> sum = a+b
>>> print("sum")
sum
>>> a = int(input("enter a value"))
enter a value
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = int(input("enter a value"))
ValueError: invalid literal for int() with base 10: ''
>>> a = int(input("enter first number:"))
enter first number:16
>>> b = int(input("enter second number:"))
enter second number:10
>>> sum=a+b
>>> print("sum:",sum)
sum: 26
>>> 
a = int(input("enter value of a:"))
enter value of a:20
>>> b = int(input("enter value of b:"))
enter value of b:60
>>> sum=a+b
>>> print("sum of a & b is:",sum)
sum of a & b is: 80
>>> 
List = []
>>> print("initial blank list:")
initial blank list:
>>> print("List")
List
>>> a=[1,4,"hey",6,8,10]
>>> a[0]
1
>>> a[2]
'hey'
>>> len(a)
6
>>> a.pop("hey")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop("hey")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop()
10
>>> a
[1, 4, 'hey', 6, 8]
>>> del a
>>> a=[1,3,5,7,9]
>>> a.sort
<built-in method sort of list object at 0x7f6d1107da08>
>>> a
[1, 3, 5, 7, 9]
>>> a=20
>>> b=30
>>> 
