s={2,3,4,35,1,67,'Hello'}
d=set()
print(type(s),type(d))
print(s)
s.add(34)
print(s)
s.add('Helloo')
print(s)
d.add(2)
d.add(23)
d.add(4)
d.add(35)
d.add("Hello")
print(s)
print(d)
print(s.union(d))
print(s.intersection(d))
print(d)
print(s-d)
print({2,4}.issubset(s))
print(s)
s.pop()
print(s)