# %%
import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
arr1

# %%
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2

# %%
arr2.ndim
# %%
arr2.shape

# %%
arr1.dtype
# %%
arr2.dtype

# %%
np.zeros(10)

# %%
np.zeros((3, 6))

# %%
np.empty((2, 3, 2))

# %%
np.arange(15)

# %%
arr = np.array([3.7, 1.2, -2.5])

arr.astype(np.int32)
