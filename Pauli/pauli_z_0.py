from pyquil import Program
from pyquil.gates import Z
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

p.inst(Z(0))

print("--- Estado final ---")
print(wfs.wavefunction(p))