import numpy as np

arr = np.arange(0,11)

print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[3:])

# BROADCAST
arr[:5] = 100
print(arr)

# copy array
newArray = arr.copy()

# indexing matrix
mat = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(mat[1:, :3])

# CONDITIONAL SELECTION
conditional_arr = np.arange(1,11)

print(conditional_arr[conditional_arr > 4])