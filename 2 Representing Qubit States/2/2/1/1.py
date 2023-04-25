from qiskit import QuantumCircuit
from math import sqrt
vector = [1/sqrt(2),1/sqrt(2)]
qc = QuantumCircuit(1)
qc.initialize(vector, 0)
qc.draw()