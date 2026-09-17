from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n = 9
s = "100111101"

qc = QuantumCircuit(n+1,n)

# prep, n is target

qc.x(n)

for i in range(n+1):
    qc.h(i)

# the oracle

for j in range(n):
    if s[::-1][j] == "1":
        qc.cx(j,n)

# second hadamard, except target

for i in range(n):
    qc.h(i)

# measure

for i in range(n):
    qc.measure(i,i)


sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=1000).result().get_counts()

print(qc.draw())
print(counts)

