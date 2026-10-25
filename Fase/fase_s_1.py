from pyquil import Program
from pyquil.gates import X, S
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program(X(0))

print("--- Estado inicial |1> ---")
print(wfs.wavefunction(p))

p.inst(S(0))

print("--- Estado final ---")
print(wfs.wavefunction(p))