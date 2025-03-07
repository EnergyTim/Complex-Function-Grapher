import numpy as np
import matplotlib.pyplot as plt

n = 200
x = np.linspace(-20, 20, n)
y = np.linspace(-20, 20, n)
z = np.zeros((n, n), dtype=complex)
black = np.zeros((n,n))

for i in range(0, n):
    for j in range(0, n):
        z[i][j] = complex(x[i], y[j])

fz = z

absfz = np.sqrt(pow(fz.real, 2)+pow(fz.imag, 2))

H = (np.arctan2(fz.imag, fz.real)%(2*np.pi))*180/np.pi
S = 1
L = (2/np.pi)*np.arctan(absfz)

print(H)
print(S)
print(L)

plt.subplot(1, 1, 1)
plt.imshow(np.rot90(H), cmap='hsv', vmin=0, vmax=360)
plt.imshow(black, cmap='gray', vmin=0, vmax=1, alpha=np.rot90(1-L))

plt.show()