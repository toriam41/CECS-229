"""
Tori McDonald
"""

import numpy as np

kobe = [[18, 7.6], [19, 15.4], [20, 19.9], [21, 22.5], [22, 28.5], [23, 25.2],
		[24, 30], [25, 24], [26, 27.6] , [27, 35.4], [28, 31.6], [29, 28.3],
		[30, 26.8], [31, 27], [32, 25.3], [33, 27.9], [34, 27.4], [35,13.8],
		[36, 22.3], [37, 17.6]]


# Part2: TODO- Make kobe into numpy array (kobe_np) and getting dimensions
kobe_np = np.array(kobe)
#print(kobe_np)
#print(type(kobe_np))

#print(kobe_np.shape)
num_rows = kobe_np.shape[0]
num_columns = kobe_np.shape[1]
#print(num_rows)
#print(num_columns)

# Part3a: TODO- Make transpose of kobe_np (kobe_transpose)
kobe_transpose = kobe_np.T
#print(kobe_transpose)


# Part3b: TODO- Ones
ones = np.ones(num_rows)
#print(ones)


# Part3c: TODO- Getting value ([18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29. 30. 31. 32. 33. 34. 35. 36. 37.])
A = kobe_transpose[0]
y = kobe_transpose[1]

#print(A)
#print(y)

# Part3d: TODO- Use column_stack
x = np.column_stack((A, ones))
#print(x)

# Part3e: TODO- Use matrix multiplication
x_prod = np.matmul(x.T, x)
#print(x_prod)

# Part3f: TODO- Find inverse
x_prod_inv = np.linalg.inv(x_prod)
#print(x_prod_inv)


# Part 4:
print("x_prod_inv:\n", x_prod_inv)

mult = np.matmul(x.T, y)
#print(mult)

theta = np.matmul(x_prod_inv, mult)
print("theta0:\n", theta[0])
print("theta1:\n", theta[1])
