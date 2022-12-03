import numpy as np

a = np.array([1,2,3], dtype='int16')
print(a)

b = np.array([[7.0,8.0,6.0],[3.0,4.0,5.0]])
print(b)

#Get Dimension(wymiar,rozmiar)
b.ndim #2

#Get Shape
b.shape #2 rows, 3 columns

#Get Type
a.dtype #int16

#Get Size
a.itemsize #2 bites

#Get total size
a.size * a.itemsize #6
# ==
a.nbytes #6
