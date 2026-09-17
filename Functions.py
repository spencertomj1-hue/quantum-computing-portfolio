from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np

def Entangle(qc, Qubit, Number = None, Range = None): # Generalise to be able to entangle qubit n with N other qubits

    if Range is None:
        qc.h(0)
        for i in range(Number):
            qc.cx(0,i+1)

    else:
        a, b = Range

        if Qubit >= a and Qubit <= b:
            raise ValueError("Cannot entangle qubit with itself, Qubit within Range")

        targets = range(a, b+1)
        qc.h(Qubit)

        for i in targets:
            qc.cx(Qubit,i)

    return qc

#mcz

def mcz(qc):
    
    n = qc.num_qubits # take nth qubit as target
    controls = list(range(n-1)) # create control list

    #machinery
    qc.h(n-1)
    qc.mcx(controls, n-1)
    qc.h(n-1)

