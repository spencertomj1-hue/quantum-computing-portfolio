from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create 3 qubits, 3 classical bits
qc = QuantumCircuit(3, 3)

#Hadamard gate, put qubit 0 into superpostiion
qc.h(0)

#Entangle 0 and 1, 0 and 2
qc.cx(0,1)
qc.cx(0,2)

#Show circuit
print(qc.draw())

#Collapse superposition
qc.measure([0, 1, 2], [0, 1, 2])

#Simulate 
sim = AerSimulator()
result = sim.run(qc, shots = 10000).result()
counts = result.get_counts()
print(counts)
