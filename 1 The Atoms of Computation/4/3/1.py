from qiskit import QuantumCircuit
qc_cnot = QuantumCircuit(2)
qc_cnot.cx(0, 1)
qc_cnot.draw()