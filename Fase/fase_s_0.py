from pyquil import Program
from pyquil.gates import S
from pyquil.api import WavefunctionSimulator

wfs = WavefunctionSimulator()
p = Program()

print("--- Estado inicial |0> ---")
print(wfs.wavefunction(p))

p.inst(S(0))

print("--- Estado final ---")
print(wfs.wavefunction(p))