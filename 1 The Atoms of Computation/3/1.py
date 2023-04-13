from qiskit import QuantumCircuit
qc_output=QuantumCircuit(8)
qc_output.measure_all()
qc_output.draw(initial_state=True)