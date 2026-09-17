#setup

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
from Functions import mcz
import matplotlib.pyplot as plt

n = 6
marked = "101101"
m = 1
N = 2**n
samples = 5000


qc = QuantumCircuit(n,n)

#prep

for i in range(n):
    qc.h(i)


def grover_iteration(qc, marked, n):

    # %%%%%%%%%  oracle  %%%%%%%%%

    zero_pos = []

    # grab pos of zeros in marked
    for ind, val in enumerate(marked):
        if val == '0':
            zero_pos.append(ind)

    # flip qubits in position of zeros in marked
    for k in zero_pos:
        qc.x(k)

    # apply multi controlled Z gate
    mcz(qc)

    # flip back
    for l in zero_pos:
        qc.x(l)


    # %%%%%%%%%  diffuser  %%%%%%%%%

    qubits = range(n)

    qc.h(qubits) # |s> basis to |0> basis

    #reflect about |0> basis
    qc.x(qubits)
    mcz(qc)
    qc.x(qubits)

    qc.h(qubits) # |0> basis to |s> basis




num_iter = int((np.pi/4)*(np.sqrt(N/m)))

for _ in range(num_iter):
    grover_iteration(qc, marked, n)

qc.measure(range(n), range(n))          # measure all qubits 
print(qc.draw())


# run
counts = AerSimulator().run(qc, shots=samples).result().get_counts()
print(marked, "got", counts.get(marked, 0), "counts")

err = ((samples - counts.get(marked, 0)) / samples )* 100
print("Error rate of", err,"%")
