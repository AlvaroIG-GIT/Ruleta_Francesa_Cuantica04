from pyquil import Program
from pyquil.gates import RX
from pyquil.api import WavefunctionSimulator
import numpy as np

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

p.inst(RX(np.pi / 2, 0))

print("--- Estado final ---")
print(wfs.wavefunction(p))