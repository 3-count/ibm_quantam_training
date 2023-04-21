from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
from math import sqrt
initial_state = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>
sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit
qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
qc.initialize(initial_state, 0) # Initialize the 0th qubit in the state `initial_state`
qc.save_statevector() # Save statevector
state = sim.run(qc).result().get_statevector() # Execute the circuit
print(state)           # Print the result
results = sim.run(qc).result().get_counts()
plot_histogram(results)