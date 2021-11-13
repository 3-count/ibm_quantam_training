from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
qc_output=QuantumCircuit(8)
qc_output.measure_all()
sim=Aer.get_backend('aer_simulator')
qobj=assemble(qc_output)
result=sim.run(qobj).result()
counts=result.get_counts()
plot_histogram(counts)