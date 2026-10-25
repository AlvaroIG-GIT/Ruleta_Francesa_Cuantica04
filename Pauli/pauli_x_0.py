from pyquil import Program
from pyquil.gates import X
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

p.inst(X(0))

print("--- Estado final ---")
print(wfs.wavefunction(p))