from pyquil import Program
from pyquil.gates import Y
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

p.inst(Y(0))

print("--- Estado final ---")
print(wfs.wavefunction(p))