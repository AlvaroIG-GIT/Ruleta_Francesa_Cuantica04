from pyquil import Program
from pyquil.gates import X, Z
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

# Construcción de Y usando la relación: Y = i * X * Z
p.inst(Z(0))
p.inst(X(0))

wf = wfs.wavefunction(p)
amplitudes_y = 1j * wf.amplitudes

print("--- Estado final construido con amplitudes y 1j ---")
print(amplitudes_y)