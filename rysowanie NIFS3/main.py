import matplotlib.pyplot as plt
def lambdak(x, k):
    hk = x[k] - x[k - 1]
    hk1 = x[k + 1] - x[k]
    return hk / (hk + hk1)

def dk(x, y, k):
    t1 = (y[k + 1] - y[k]) / (x[k + 1] - x[k])
    t2 = (y[k] - y[k - 1]) / (x[k] - x[k - 1])
    return 6 * (t1 - t2) / (x[k + 1] - x[k - 1])

def moments(t, x, y):
    n = len(t) - 1
    q = [0]
    p = [0]
    ux = [0]
    uy = [0]
    for i in range(1, n):
        lk = lambdak(t, i)
        p.append(lk * q[i - 1] + 2)
        q.append((lk - 1) / p[i])
        dk_ = dk(t, x, i)
        ux.append((dk_ - lk * ux[i - 1])/p[i])
        dk_ = dk(t, y, i)
        uy.append((dk_ - lk * uy[i - 1])/p[i])

    Mx, My = [0]*(n+1), [0]*(n+1)
    Mx[n], My[n] = 0, 0
    Mx[n-1], My[n-1] = ux[n-1], uy[n-1]
    for i in range(n-2, -1, -1):
        Mx[i] = ux[i] + q[i] * Mx[i + 1]
        My[i] = uy[i] + q[i] * My[i + 1]

    return Mx, My

def nifs3(X, x0, y0, M):
    k = 1
    while x0[k] < X:
        k += 1

    return (1/(x0[k]-x0[k-1])) * (M[k-1]*pow(x0[k] - X, 3)/6. +  M[k] * pow(X - x0[k-1], 3)/6. + (y0[k-1] - M[k-1]*pow(x0[k]-x0[k-1], 2)/6.)*(x0[k]-X) + (y0[k] - M[k]*pow(x0[k]-x0[k-1], 2)/6.)*(X-x0[k-1]))

def ts(n):
    n-=1
    t = []
    for k in range(n+1):
        t.append(k/n)
    return t


def read_coordinates_from_file(file_path):
    X, Y = [], []

    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 2:
                x, y = map(float, values)
                X.append(x)
                Y.append(y)

    return X, Y

m_val = [60,20,30,60,70,10,30,60,60,50,60,20,20,10,20]
z = 0
while z < 15:
    x0, y0 = read_coordinates_from_file(f"{z}.txt")
    t = ts(len(x0))
    Mx, My = moments(t, x0, y0)
    M = m_val[z]
    nifsx = []
    nifsy = []
    for k in range(M+1):
        nifsx.append(nifs3(k/M, t, x0, Mx))
        nifsy.append(nifs3(k/M, t, y0, My))

    plt.plot(nifsx, nifsy)
    z += 1




fig, ax = plt.subplots()

width,height = 1161,171
aspect_ratio = width / height

ax.set_xlim(0, width)
ax.set_ylim(0, height)
fig.set_size_inches(8, 8 / aspect_ratio)

plt.show()



