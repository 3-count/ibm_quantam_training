from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
qc_encode = QuantumCircuit(8)
qc_encode.x(7)
qc_encode.draw()
qc_encode.measure_all()
qc_encode.draw()
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc_encode).result()
counts = result.get_counts()
plot_histogram(counts)