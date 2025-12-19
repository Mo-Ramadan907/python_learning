import numpy as np
#_-----introduction of numpy
# print(np.__version__)
# lst = [1,2,3,4,5]
# array = np.array(lst)
# array *=2
# print(array)

array = np.array([[["a","b","c"],["d","e","f"],["g","h","i"]],
                  [["j","k","l"],["m","n","o"],["p","q","r"]],
                  [["s","t","u"],["v","w","x"],["y","z"," "]],
                  ])

# print(array.ravel())
# characters = array[2,0,:]
# print(characters)
# array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(array[2:,2:]) 

array = np.array([1.01,2.8,3.88])
# print(array+2)
# print(array*3)
# print(array/4)
# print(array%3)
# print(np.sqrt(array))
# print(np.round(array))
# print(np.ceil(array))
# print(np.pi)
# radii = np.array([1,2,3])


array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
# print(array1.dot(array2))
# print(array1 / array2)

# print(np.linalg.norm(array1))

random_nums = np.random.default_rng()
# print(random_nums.integers(low=0,high=10,size=(5)))
# print(random_nums.random(size=(2,2),dtype=np.float32))

# print(len(array1))
# print(np.linspace(0,6,7))
# print(np.full((3,3),1))
# print(np.zeros((3,3,3)))
# print(np.eye(5))
# array = np.array([[10,11,12,123],[8,9,23,1983]])
# print(np.full_like(array,10))
# print(np.ones_like(array))
# print(np.arange(0,10,2))
# print(np.arange(0,10,3))


# print(np.zeros((3,3),dtype=np.float64))

# print(array.dtype)
# print(array.reshape())
# print(array.ravel())


# np.random.rand(3, 3)
# np.random.randn(3, 3)
# np.random.randint(0, 10, (3,3))
# np.random.choice([1,2,3], size=4)
# np.random.seed(42)

randomness = np.random.default_rng()
random_arr = randomness.random(size=(5,5),dtype=np.float32)
# print(random_arr)
for i in range(random_arr.shape[0]):
    print(random_arr[i].mean())
    print(random_arr[i].max())
    print("#_____#")

arr = np.array([i for i in range(1,101)])
even_arr = arr[arr % 2 == 0 ]
# print(even_arr)
# divisble_7 = arr[arr%7==0]
# print(divisble_7)


matrixA = randomness.random(size=(3,3),dtype=np.float32)
matrixB = randomness.random(size=(3,3),dtype=np.float32)
# print(matrixA @ matrixB)
matrix_c = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]],dtype=np.float32)
# print(matrixA @ matrixB)

# print(np.linalg.det(matrixA))

# print(matrixA.diagonal())

print(matrixA)
nor = np.linalg.matrix_norm(matrixA)
for i in range(matrix_c.shape[0]):
    for j in range(matrix_c.shape[1]):
        matrixA[i][j] /= nor

print(matrixA)


# Random 5x5 matrix
randomness = np.random.default_rng()
random_arr = randomness.random(size=(5,5), dtype=np.float32)

# Row mean & max
for i in range(random_arr.shape[0]):
    print(random_arr[i].mean())
    print(random_arr[i].max())
    print("#_____#")

# 1 to 100 array
arr = np.arange(1, 101)

even_arr = arr[arr % 2 == 0]
divisible_7 = arr[arr % 7 == 0]

# Random matrices A and B
matrixA = randomness.random(size=(3,3), dtype=np.float32)
matrixB = randomness.random(size=(3,3), dtype=np.float32)

# Matrix multiplication
product = matrixA @ matrixB

# Determinant
det_A = np.linalg.det(matrixA)

# Diagonal
diag_A = matrixA.diagonal()

# Normalization
norm_value = np.linalg.norm(matrixA)
matrixA_normalized = matrixA / norm_value

print("Original A:\n", matrixA)
print("Normalized A:\n", matrixA_normalized)



temp_matrix = randomness.random(size=(10,10),dtype=np.float32)
# for i in range(temp_matrix.shape[1]):
#     print(temp_matrix[:,i].sum())

for i in range(temp_matrix.shape[0]):
    print(temp_matrix[i].min())

temp_matrix[temp_matrix< 0.2] = 0


temp_matrix = np.arange(50,100)
temp_matrix = temp_matrix[(temp_matrix % 3 !=0) & (temp_matrix % 5 !=0)]
print(len(temp_matrix[temp_matrix % 7 ==0]))


temp_matrix = np.eye(6)
print(temp_matrix * 10 )

temp_matrix *= 10
temp_matrix[temp_matrix ==10] = 15 

temp_matrix = randomness.random(size=(1,20),dtype=np.float32)

print(temp_matrix.mean())
print(temp_matrix.std())
print(temp_matrix.var())
print(np.median(temp_matrix))

temp_matrix /= np.linalg.norm(temp_matrix)

#---- level 2 

temp_matrix = randomness.random(size=(4,4),dtype=np.float32)
print(temp_matrix)

temp_matrix[0],temp_matrix[3] = temp_matrix[3].copy() , temp_matrix[0].copy()

print(temp_matrix)

temp_matrix[:,1] , temp_matrix[:,2] = temp_matrix[:,2].copy(),temp_matrix[:,1].copy()

print(temp_matrix)

temp_matrix = temp_matrix[::-1,::-1]
print(temp_matrix)


temp_matrix = randomness.integers(low =1 ,high=26,size=(5,5))
print(temp_matrix)
print(temp_matrix[:,0],temp_matrix[0,:],temp_matrix[:,-1],temp_matrix[-1,:])



#---hard 

matrixA = randomness.random(size=(4,4))

matrixB = randomness.random(size=(4,4))

c = np.multiply(matrixA,matrixB) + matrixA + matrixB
print(c)

d = matrixA @ matrixB - matrixB @ matrixA
print(d)


matrixA_norm = (matrixA - matrixA.min() ) / (matrixA.max() - matrixA.min())
print(matrixA_norm)
