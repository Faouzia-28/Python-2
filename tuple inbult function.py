Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="teddy"
a=list(a)
a
['t', 'e', 'd', 'd', 'y']
a=tuple(a)
a
('t', 'e', 'd', 'd', 'y')
type(a)
<class 'tuple'>
a[2:4]
('d', 'd')
a.count(d)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.count(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
a.count("d")
2
a.count('a')
0
a.index('y')
4
a.index("d")
2
(a,b,c)=(1,2,3)
b
2
a
1
c
3
(l,k,m)=(1,2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (l,k,m)=(1,2)
ValueError: not enough values to unpack (expected 3, got 2)
>>> a
1
>>> a='teddy'
>>> a=tuple(a)
>>> a
('t', 'e', 'd', 'd', 'y')
>>> a*3
('t', 'e', 'd', 'd', 'y', 't', 'e', 'd', 'd', 'y', 't', 'e', 'd', 'd', 'y')
>>> a
('t', 'e', 'd', 'd', 'y')
>>> 'a' in a
False
>>> 'd' in a
True
>>> 'a' not in a
True
>>> b='bear'
>>> b=tuple(b)
>>> b
('b', 'e', 'a', 'r')
>>> a is b
False
>>> a is not bb
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a is not bb
NameError: name 'bb' is not defined. Did you mean: 'b'?
>>> a is not b
True
