from qiskit import QuantumCircuit ,Aer
from qiskit.visualization import plot_bloch_multivector
from math import sqrt

qc = QuantumCircuit(3)
vector = [sqrt(3)/2, 1.j/2]
qc.initialize(vector, 0)
qc.initialize(vector, 1)
qc.initialize(vector, 2)
qc.h(1)
qc.z(1)
qc.h(1)
qc.x(2)
sim = Aer.get_backend('aer_simulator')
# Let's see the result
qc.save_statevector()
state = sim.run(qc).result().get_statevector()
plot_bloch_multivector(state)