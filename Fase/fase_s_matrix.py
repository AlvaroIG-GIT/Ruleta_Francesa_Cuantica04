import numpy as np

M_s = np.array([[1, 0], [0, 1j]], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

resultado = M_s @ ket_1

print("Matriz S:\n", M_s)
print("Vector |1>:", ket_1)
print("Multiplicación M @ |1>:", resultado)