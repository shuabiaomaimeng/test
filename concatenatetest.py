a = np.random.randint(low=0,high=3,size=(2, 2, 1))
b = np.random.randint(low=0,high=3, size=(2, 2, 1))
print('----------------------------------a')
print(a.shape)
print(a)
print(a[0][0][0])
print(a[0][1][0])
print(a[1][0][0])
print(a[1][1][0])
print('----------------------------------b')
print(b.shape)
print(b)
print(b[0][0][0])
print(b[0][1][0])
print(b[1][0][0])
print(b[1][1][0])
print('----------------------------------b')
c = np.concatenate((a, b), axis=-1)
print(c.shape)
print(c[0][0][0])
print(c[0][1][0])
print(c[1][0][0])
print(c[1][1][0])
print(c[0][0][1])
print(c[0][1][1])
print(c[1][0][1])
print(c[1][1][1])
