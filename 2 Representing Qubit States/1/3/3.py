from qiskit import QuantumCircuit, Aer
from qiskit.visualization import plot_histogram
sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit
qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
initial_state = [0,1]   # Define initial_state as |1>
qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
qc.save_statevector()   # Tell simulator to save statevector
result = sim.run(qc).result() # Do the simulation and return the result
qc.measure_all()
counts = result.get_counts()
plot_histogram(counts)