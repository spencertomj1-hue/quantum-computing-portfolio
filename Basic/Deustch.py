from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2,1)

# get a 0 and 1 qubit
qc.x(1)

# hadamard both to get |+> input, |-> target
qc.h(0)
qc.h(1)

# Apply oracle

qc.cx(0,1)

# Apply final hadamard 
qc.h(0)

# draw circuit
print(qc.draw())

# measure
qc.measure(0,0)

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1000).result().get_counts()
print(counts)