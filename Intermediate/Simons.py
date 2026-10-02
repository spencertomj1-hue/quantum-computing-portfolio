import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt
from Functions import RREF


def run_simon(n, s, shots=1000):

    def simon_circuit(qc,n,s):
        # hadamard input register
        qc.h(range(n))

        def simon_oracle(qc, n, s):
            #copy input to output register
            for i in range(n):
                qc.cx(i,n + i)

            # control qubit chosen in pos of s = 1 therefore x and x xor s are opposite here
            j = s.index('1')

            for k in range(n):

                # determine which of x, x xor s qubits need to flipped 
                if s[k] == '1':
                    # flip n+k th bit enforcing f(x) = f(x xor s)
                    qc.cx(j,n+k)

        simon_oracle(qc,n,s)

        #collapse output register
        qc.measure(range(n, 2*n), range(n))
        qc.barrier()

        # hadamard input register
        qc.h(range(n))

        qc.measure(range(n), range(n))

    qc = QuantumCircuit(2*n, n)
    simon_circuit(qc, n, s)
    sim = AerSimulator()
    counts = sim.run(qc, shots=shots).result().get_counts()
    print(qc.draw())
    print(counts)

    return(counts)

counts = run_simon(5, '11010')

rows = [[int(b) for b in key[::-1]] for key in counts if '1' in key]

M = np.array(rows, dtype=int)

s = RREF(M)

print(s)