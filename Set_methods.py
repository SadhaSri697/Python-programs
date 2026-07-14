set = {90,78,5,678,678,"Sadha"}
print(set, type(set))
# repetion is not allowed in sets
set.add(56)
print(set , type(set))

s = {1, 2, 3}
s.remove(2)
print(s)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))

s = {1, 2, 3}
s.discard(3) # discard means to remove
print(s)

# differ btw discard and remove
# discard no error
# remove we get error 
s = {1, 2, 3}
s.pop()     # it removes random element
print(s)