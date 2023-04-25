from qiskit import QuantumCircuit ,Aer
from qiskit.visualization import plot_bloch_multivector
from math import sqrt
vector = [1/sqrt(2), -1/sqrt(2)]
qc = QuantumCircuit(2)
qc.initialize(vector, 0)
qc.initialize(vector, 1)
qc.x(0)
sim = Aer.get_backend('aer_simulator')
qc.save_statevector()
state = sim.run(qc).result().get_statevector()
plot_bloch_multivector(state)