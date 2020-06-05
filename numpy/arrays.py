import numpy as np

# Creating Numpy Array
my_list = [1,2,3]
x = np.array(my_list)
print(type(x))

print("\n"*2)
# Matrix
matrix = [[1,2,3], [4,5,6], [7,8,9]]
y = np.array(matrix)
print(y)

print("\n"*2)
# numpy version of range()
# also has start, stop(excluded), stepsize
r = np.arange(0,5)
print(r)

print("\n"*2)
# generate arrays of zeros and ones
z = np.zeros(5)
print(z)

# zeros matrix
z2 = np.zeros((4,5))
print(z2)

o = np.ones(5)
print(o)

o2 = np.ones((4,5))
print(o2)

print("\n"*2)
# linear space
# spacing numbers evenly within a range
l = np.linspace(0,10,51)
print(l)

print("\n"*2)
# Identity matrix
# identity matrix is a square, rows and columns are equal and diagonal is 1
i = np.eye(4)
print(i)

print("\n"*2)
# random
# uniform distribution
rand = np.random.rand(1)
print(rand)

rand2 = np.random.rand(5,4)
print(rand2)

# standard distribution
rand3 = np.random.randn(5)
print(rand3)

rand4 = np.random.randn(5,4)
print(rand4)

# random integer
randomint = np.random.randint(1, 100)
print(randomint)

print("\n"*2)
# reshape array
arr = np.array(list(range(25)))
arr = arr.reshape(5,5)
print(arr)
print(arr.shape)


# get type inside array
print(arr.dtype)

# min max
print("\n"*2)
random_arr = np.random.randint(1, 100, 10)
print(random_arr)
print(random_arr.max())
print(random_arr.argmax()) # index of max
print(random_arr.min())
print(random_arr.argmin()) # index of max