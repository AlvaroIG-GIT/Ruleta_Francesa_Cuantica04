from pyquil import Program
from pyquil.gates import X, RZ
from pyquil.api import WavefunctionSimulator
import numpy as np

wfs = WavefunctionSimulator()
p = Program(X(0))

print("--- Estado inicial |1> ---")
print(wfs.wavefunction(p))

p.inst(RZ(np.pi / 2, 0))

print("--- Estado final ---")
print(wfs.wavefunction(p))