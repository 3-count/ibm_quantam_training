from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
from math import sqrt
vector = [1.j/sqrt(3), sqrt(6)/3]
qc = QuantumCircuit(1)
qc.initialize(vector, 0)
sim = Aer.get_backend('aer_simulator')
qc.save_statevector()
results = sim.run(qc).result().get_counts()
plot_histogram(results)