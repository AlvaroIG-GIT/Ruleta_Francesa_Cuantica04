from pyquil import Program
from pyquil.gates import X, PHASE, S, T, Z
from pyquil.api import WavefunctionSimulator
import numpy as np

wfs = WavefunctionSimulator()

# Demostración comparativa de equivalencias sobre |1>
circuitos = {
    "S": Program(X(0), S(0)),
    "PHASE(pi/2)": Program(X(0), PHASE(np.pi / 2, 0)),
    "T": Program(X(0), T(0)),
    "PHASE(pi/4)": Program(X(0), PHASE(np.pi / 4, 0)),
    "Z": Program(X(0), Z(0)),
    "PHASE(pi)": Program(X(0), PHASE(np.pi, 0)),
    "S^2": Program(X(0), S(0), S(0)),
    "T^2": Program(X(0), T(0), T(0))
}

for nombre, p in circuitos.items():
    print(f"{nombre}:", wfs.wavefunction(p))