import numpy as np

theta = np.pi / 3
M_phase = np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

resultado = M_phase @ ket_1

print("Matriz PHASE(pi/3):\n", M_phase)
print("Vector |1>:", ket_1)
print("Multiplicación M @ |1>:", resultado)