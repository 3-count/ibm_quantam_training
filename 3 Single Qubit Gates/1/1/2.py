from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_bloch_multivector
# Let's do an X-gate on a |0> qubit
qc = QuantumCircuit(1)
qc.x(0)
sim = Aer.get_backend('aer_simulator')
# Let's see the result
qc.save_statevector()
state = sim.run(qc).result().get_statevector()
plot_bloch_multivector(state)