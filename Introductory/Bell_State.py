from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Creates 2 qubits, 2 classical bits
qc = QuantumCircuit(2, 2)

# Puts qubit 0 into superposition |0,0>
q0 = qc.h(0)

# CNOT -> Puts qubit 1 only if qubit 0 is 1, as qubit 0 is in superposition, 
# this entangles qubit 0 and 1, gives state Norm(|00> + |11>)
qc.cx(0,1)

# Shows diagram of circuit
print(qc.draw())

#Collapse superposition
qc.measure([0, 1], [0, 1])

# Now simulate
sim = AerSimulator()
result = sim.run(qc, shots = 10000).result()
counts = result.get_counts()
print(counts)

