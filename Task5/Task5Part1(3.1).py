#Data Structures and Sequence in Python
# Task 5
# 1.TUPLES

tup = tuple('hello')
print(tup)
tup1 = tuple([1, 2, 3, 4, 5])
print(tup1)
tuple = 1, 2.5, 'hello', True
print(tuple)
print(len(tuple))

#Accessing elements in a tuple
print(tup[1])

#Nested tuples
tup3 = (1, 2, 3), (4, 5)
print(tup3)
print(len(tup3))
print(tup3[1])

tup2 = (1,[1,2],False)
#   tup2[1] = False #TypeError: 'tuple' object does not support item assignment
print(tup2)
tup2[1].append(3) #No error
print(tup2)

#Concatenation
tup4 = (1, 2, 3) + (4, 5, 6,'Foo') + ('Hello',)
print(tup4)

tup = ('foo','boo')*4
print(tup)

#Unpacking tuples
tup = ('foo', 'bar', 'baz')
a, b, c = tup
print(a)

tup = 4, 5, (6, 7)
a, b, (c, d) = tup
print(d)  # Output: 7

a, b = 1, 2
print(a)  # Output: 1
print(b)  # Output: 2

b, a = a, b
print(a)  # Output: 2
print(b)  # Output: 1

#Iterating through a tuple
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}')
# Output:
# a=1, b=2, c=3
# a=4, b=5, c=6
# a=7, b=8, c=9

#Extended unpacking
values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a)  # Output: 1
print(b)  # Output: 2
print(rest)  # Output: [3, 4, 5]

#  *_ Ignore some values
a, b, *_ = values          
print(a)  # Output: 1
print(b)  # Output: 2

a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))  # Output: 4 

#Lists
list1 = [1,2,3,None]
print(list1)
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
print(b_list)
gen = range(10)
c_list = list(gen)
print(c_list)
d_list = list('hello')
print(d_list)
b_list.append('dwarf')
print(b_list)
b_list.insert(1, 'red')
print(b_list)
b_list.pop(2)
print(b_list)
b_list.remove('foo')
print(b_list)
"dwarf" in b_list
print("dwarf" in b_list)
"dwarf" not in b_list
print("dwarf" not in b_list)

#Concatenation and combining lists
[4, None, 'foo'] + [7, 8, (2, 3)]
print([4, None, 'foo'] + [7, 8, (2, 3)])
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
print(x)

#Sorting
a = [7, 2, 5, 1, 3]
a.sort()
print(a)
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)

#Slice
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq.sort()
print(seq[1:5])
print(seq[3:4])
print(seq[:5])
print(seq[3:])
print(seq[-4:])     #Negative indices slice the sequence relative to the end
print(seq[-6:-2])    #Negative indices slice the sequence relative to the end


#Dictionaries
d1 = {"a":[1,2,3] , "b": "Biha"}
print(d1['b'])
print('b' in d1)
del d1['a']
print(d1)
d2 = {'a': 'some value',
'b': [1, 2, 3, 4],
7: 'an integer',
5: 'some value',
'dummy': 'another value'}
d2.pop('dummy')
print(list(d2.keys()))
print(list(d2.values()))
print(list(d2.items()))               #items give both key and values


#Sets
a = set([2,1,3,1,4])
print(a)
b = set([9,0,8,7])
print(a.union(b))
print(a & b)

#Built-In Sequence functions 
#Enumerate

#Old method 
# def enumer:
    
#     index = 0
#     for i in a:
#       index+=1

# #Built in method
#     for index,i in enumerate(a):
#      #Required function
    
#Sorted 
sorted([2,1,3,1,4])
seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]
zipped = zip(seq1, seq2)
print(list(zipped)) 
seq3 = [False, True]
print(list(zip(seq1, seq2, seq3)))


#Reverse
print(list(reversed(range(10,100))))
