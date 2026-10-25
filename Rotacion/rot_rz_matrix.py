import numpy as np

theta = np.pi / 2
M_rz = np.array([
    [np.exp(-1j * theta / 2), 0],
    [0, np.exp(1j * theta / 2)]
], dtype=complex)

ket_0 = np.array([1, 0], dtype=complex)
resultado = M_rz @ ket_0

print("Matriz RZ(pi/2):\n", np.round(M_rz, 4))
print("Vector |0>:", ket_0)
print("Multiplicación M @ |0>:", np.round(resultado, 4))