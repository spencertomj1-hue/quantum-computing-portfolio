#setup

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
from Functions import mcz
import matplotlib.pyplot as plt


def Grovers_algo(n,marked_list,samples):

    qc = QuantumCircuit(n,n)

    #values
    N = 2**n
    m = len(marked_list)
    num_iter = int((np.pi/4)*(np.sqrt(N/m)))

    #prep

    for i in range(n):
        qc.h(i)


    def grover_iteration(qc, marked_list, n):

        # %%%%%%%%%  oracle  %%%%%%%%%

        # grab pos of zeros in marked
        for marked in marked_list:
            zero_pos = []
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

    # Run grover r times
    for _ in range(num_iter):
        grover_iteration(qc, marked_list, n)
    # measure all qubits 
    qc.measure(range(n), range(n))          

    # run
    counts = AerSimulator().run(qc, shots=samples).result().get_counts()
    for marked in marked_list:
        print(marked, "got", counts.get(marked, 0), "counts")
    total = sum(counts.get(mk, 0) for mk in marked_list)
    err = ((samples - total) / samples) * 100
    print("Error rate of", round(err, 2), "%")

list = "101110", "011011"
Grovers_algo(6,list,5000)