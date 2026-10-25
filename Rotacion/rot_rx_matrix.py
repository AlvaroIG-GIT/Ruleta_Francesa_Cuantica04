import numpy as np

theta = np.pi / 2
M_rx = np.array([
    [np.cos(theta / 2), -1j * np.sin(theta / 2)],
    [-1j * np.sin(theta / 2), np.cos(theta / 2)]
], dtype=complex)

ket_0 = np.array([1, 0], dtype=complex)
resultado = M_rx @ ket_0

print("Matriz RX(pi/2):\n", np.round(M_rx, 4))
print("Vector |0>:", ket_0)
print("Multiplicación M @ |0>:", np.round(resultado, 4))