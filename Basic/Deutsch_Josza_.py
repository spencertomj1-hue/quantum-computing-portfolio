from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n = 10
# n qubits but also an extra target qubit
qc = QuantumCircuit(n + 1,n)

# prep target 
qc.x(n)

# Hadamard all
for i in range(n+1):
    qc.h(i)

# Apply oracle

for i in range(n):
    qc.cx(i,n)

# Second hadamard except on target

for i in range(n):
    qc.h(i)

# now measure

for i in range(n):
    qc.measure(i,i)

# report results

sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1000).result().get_counts()

print(qc.draw())
print(counts)

# result -> {'1111111111': 1000} therefore 3

