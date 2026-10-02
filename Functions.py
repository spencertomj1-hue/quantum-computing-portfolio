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


def RREF(M):

    n = len(M[0,:])
    rowcount = 0
    pivots = np.zeros(n)

    # walks colum L-R
    for col in range(n):

        pivot_ind = None
        # for this column find a row with a 1, take this row as the pivot
        for row in range(rowcount, len(M)): 

            if M[row,col] == 1:
                pivot_ind = row
                break

        # if no pivot found go to next column
        if pivot_ind is None:
            continue
            
        # switch pivot and working row
        dum1 = M[pivot_ind, :].copy()
        dum2 = M[rowcount,:].copy()

        M[pivot_ind, :] = dum2
        M[rowcount,:] = dum1

        # xor pivot row into every row with a 1 in this column
        for row in range(len(M)):
            if M[row ,col] == 1 and row !=rowcount:
                M[row ,:] =  M[row, :] ^ M[rowcount, :]

        # move down working row
        rowcount += 1

        # track pivots
        pivots[col] += 1

    checker = 0

    # finding free column
    for i in range(len(pivots)):
        if pivots[i] == 0:
            free_col = i
            checker += 1

    # warnings
    if checker > 1:
        raise ValueError('Too many free columns found')
    
    if checker == 0:
        raise ValueError('No free column found')


    s = M[:n, free_col].copy()   # pivot bits sit in rows 0..n-2 after RREF
    s[free_col] = 1              # force free bit to 1 (nonzero solution)

    return ''.join(str(b) for b in s)