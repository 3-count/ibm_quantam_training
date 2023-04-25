import numpy as np
import numpy.linalg as la
from qiskit import QuantumCircuit ,Aer
from qiskit.visualization import plot_bloch_multivector
y = np.array([[0,-1.j],[1.j,0]])
values, vectors = la.eig(y)

qc = QuantumCircuit(2)
qc.initialize(vectors[0], 0)
qc.initialize(vectors[1], 1)
sim = Aer.get_backend('aer_simulator')
# Let's see the result
qc.save_statevector()
state = sim.run(qc).result().get_statevector()
plot_bloch_multivector(state)