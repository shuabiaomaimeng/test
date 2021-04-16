import numpy as np
a1 = []
b1 = []
c1 = []
a = np.random.randint(0, 3, size=(3, 3, 3))
print(a)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            # print(a[i][j][k])
            a1.append(a[i][j][k])
b = np.reshape(a=a, newshape=(3, 9), order='C')
print(b)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        b1.append(b[i][j])

if (len(a1) == len(b1)):
    for i in range(len(a1)):
        print('a1[' + '%d' % i + ']=' + '%d' % a1[i])
        print('b1[' + '%d' % i + ']=' + '%d' % b1[i])
c = np.reshape(a=b, newshape=(3, 3, 3), order='C')

for i in range(c.shape[0]):
    for j in range(c.shape[1]):
        for k in range(c.shape[2]):
            # print(a[i][j][k])
            c1.append(c[i][j][k])
if (len(a1) == len(c1)):
    for i in range(len(a1)):
        print('a1[' + '%d' % i + ']=' + '%d' % a1[i])
        print('c1[' + '%d' % i + ']=' + '%d' % c1[i])
