import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
from Functions import mcz
import matplotlib.pyplot as plt