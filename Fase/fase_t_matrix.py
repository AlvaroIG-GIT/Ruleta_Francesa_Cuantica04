import numpy as np

M_t = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

resultado = M_t @ ket_1

print("Matriz T:\n", M_t)
print("Vector |1>:", ket_1)
print("Multiplicación M @ |1>:", resultado)