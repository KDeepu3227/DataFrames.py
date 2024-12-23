###
matrix
###
1)take 2*3 matrices find out what transpose and reshape matrix do
2)change matrix into a 3*4 matrix (reshape)
3)generate an array of 6 elements using arrange function.create 2*3 and 3*2 matrix from it?
4)mean
5)random number generation
###
import numpy as np
arr = np.array([1,2,3])*([1],[2],[3])
print(arr)
import numpy as np
arr = (np.array([[1],[2],[3]])*([1,2,3]))
print(arr)
import numpy as np
arr = np.array([1,2,3])*([1,2,3])
print(arr)
@@import numpy as np
arr1=np.array([[1,2,3]])
arr2=np.array([[1,2],[3,4],[5,6]])
res1=np.matmul(arr1,arr2)
print(res1)
@@import numpy as np
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
res1 =(arr1+arr2)
print(res1)
@@import  numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
res1= np.transpose(arr1)
print(res1)
res2 = np.reshape(arr1,[3,2])
print(res2)
res3 = np.resize(arr1,[3,2])
print(res3)
@@import numpy as np
a = np.arange(12)
b = np.reshape(a,[3,4])
print(b)
c = np.resize(a,[3,4])
print(c)
@@import numpy as np
a = np.arange(6)
b= np.reshape(a,[3,2])
print(b)
c= np.reshape(a,[2,3])
print(c)
@@import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
b = np.mean(arr1,axis=0)
print(b)
rand_arr = np.random.rand(5)
print(rand_arr)
###
[[1 2 3]
 [2 4 6]
 [3 6 9]]
[[1 2 3]
 [2 4 6]
 [3 6 9]]
[1 4 9]
[[22 28]]
[[ 6  8]
 [10 12]]
[[1 4]
 [2 5]
 [3 6]]
[[1 2]
 [3 4]
 [5 6]]
[[1 2]
 [3 4]
 [5 6]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[0 1]
 [2 3]
 [4 5]]
[[0 1 2]
 [3 4 5]]
[2.5 3.5 4.5]
[0.59572414 0.93183785 0.86678921 0.84219654 0.14597589]


