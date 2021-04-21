# %%
import numpy as np
# %%
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a)
print(b)
print(c)
# %%
print(a[1])
# %%
print(b[:, 1])
# %%
print(c[0, 0, :])
# %%
print(c.shape)
# %%
print(c.dtype)
# %%
cc = np.array([1, 2, 3], dtype='float64')
print(cc)
print(cc.dtype)
# %%
b[:, 2] = 8
print(b)
# %%
print(np.zeros(5))
print(np.zeros((2, 3)))

# %%
print(np.ones(4))
# %%
print(np.full((2, 4), 87))
# %%
print(np.random.rand(2, 5, 2))
# %%
print(np.random.randint(0, 100, 10))
# %%
print(np.identity(5))
# %%
print(np.eye(5, 5))
# %%
a = np.array([1, 2, 3, 4])
b = a.copy()
a[2] = 5
print(a)
print(b)
# %%
a = np.array([1, 2, 3, 4])
b = a
a[2] = 5
print(a)
print(b)
# %%
a = [1, 2]
print(a + 2)
# %%
a = np.array([1, 2])
print(a + 2)
# %%
print(np.sin(a/2))
# %%
a = np.array([[1, 2], [8, 9]])
b = np.array([[9, 7], [5, 15]])
c = np.matmul(a, b)
print(np.linalg.det(c))
print(np.linalg.det(np.identity(3)))
# %%
print(np.min(a))
print(np.max(a))
print(np.sum(a))
# %%
print(np.min(a, axis=0))
print(a)
# %%
a = np.array([1, 2, 3, 4])
b = np.reshape(a, (2, 2))
print(b)
# %%
c = np.transpose(b)
print(c)
# %%
d = b.T
print(d)
# %% hstack vstack column-stack
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = np.hstack((a, b))
print(c)
# %%
d = np.vstack((a, b))
print(d)
# %%
e = np.column_stack((a, b))
print(e)
# %%
