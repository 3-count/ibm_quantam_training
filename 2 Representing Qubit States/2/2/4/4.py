from qiskit import QuantumCircuit, Aer
from math import sqrt
qc = QuantumCircuit(1) # We are redefining qc
initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]
qc.initialize(initial_state, 0)
qc.measure_all()
sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit
qc.save_statevector()
result = sim.run(qc).result()
state = result.get_statevector()
print("State of Measured Qubit = " + str(state))
