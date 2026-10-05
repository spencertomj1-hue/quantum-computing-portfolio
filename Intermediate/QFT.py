from qiskit import QuantumCircuit
from numpy import pi
from qiskit.quantum_info import Statevector
import numpy as np


def QFT(qc):

    n = qc.num_qubits
    for j in range(n):
        qc.h(j) # applies coarse phase to jth qubit

        for k in range(j+1,n):
            angle = pi / 2**(k-j) # using qubits below the jth, apply a finer phase, as j increase the max finest phase gets coarser and coarser
            qc.cp(angle, k, j)

    qc.barrier()

    for i in range(n//2):
        qc.swap(i,n-1-i)

def test_QFT(n):
    Q = 2**n
    for x in range(Q):                      # check every input
        qc = QuantumCircuit(n)
        for i in range(n):                  # prepare |x>, qubit 0 = MSB
            if (x >> (n-1-i)) & 1:
                qc.x(i)
        QFT(qc)
        got = Statevector(qc).reverse_qargs().data   # read big-endian
        want = np.array([np.exp(2j*np.pi*x*k/Q) for k in range(Q)]) / np.sqrt(Q)
        assert np.allclose(got, want), f"fail at x={x}"
    print(f"n={n}: all {Q} inputs match")


n = 10

test_QFT(n)