from qiskit import transpile, QuantumCircuit, ClassicalRegister, QuantumRegister
import qiskit
from qiskit_aer import Aer, noise
from qiskit.visualization import plot_histogram
import math
import matplotlib.pyplot as plt

def circuit_amod15(qc, qr, cr, a):
    if a == 2:
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[1], qr[0])
    elif a == 7:
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])
    elif a == 8:
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[3], qr[2])
    elif a == 11:
        qc.cswap(qr[4], qr[2], qr[0])
        qc.cswap(qr[4], qr[3], qr[1])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])
    elif a == 13:
        qc.cswap(qr[4], qr[3], qr[2])
        qc.cswap(qr[4], qr[2], qr[1])
        qc.cswap(qr[4], qr[1], qr[0])
        qc.cx(qr[4], qr[3])
        qc.cx(qr[4], qr[2])
        qc.cx(qr[4], qr[1])
        qc.cx(qr[4], qr[0])

def circuit_aperiod15(qc, qr, cr, a):
    if a == 11:
        circuit_11period15(qc, qr, cr)
        return

    #q[0] to |1>
    qc.x(qr[0])

    #a**4 mod 15
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, pow(a, 4, 15))
    qc.h(qr[4])
    qc.measure(qr[4], cr[0])
    qc.reset(qr[4])

    #a**2 mod 15
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, pow(a, 2, 15))
    qc.u(math.pi / 2, 0, 0, qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    qc.measure(qr[4], cr[1])
    qc.reset(qr[4])

    #a mod 15
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, a)
    qc.u(3 * math.pi / 4, 0, 0, qr[4]).c_if(cr, 3)
    qc.u(math.pi / 2, 0, 0, qr[4]).c_if(cr, 2)
    qc.u(math.pi / 4, 0, 0, qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    qc.measure(qr[4], cr[2])

def circuit_11period15(qc, qr, cr):
    qc.x(qr[0])
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, pow(11, 4, 15))
    qc.h(qr[4])
    qc.measure(qr[4], cr[0])
    qc.reset(qr[4])
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, pow(11, 2, 15))
    qc.u(math.pi / 2, 0, 0, qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    qc.measure(qr[4], cr[1])
    qc.reset(qr[4])
    qc.h(qr[4])
    circuit_amod15(qc, qr, cr, 11)
    qc.u(3 * math.pi / 4, 0, 0, qr[4]).c_if(cr, 3)
    qc.u(math.pi / 2, 0, 0, qr[4]).c_if(cr, 2)
    qc.u(math.pi / 4, 0, 0, qr[4]).c_if(cr, 1)
    qc.h(qr[4])
    qc.measure(qr[4], cr[2])

noise_model = noise.NoiseModel()
error_1 = noise.depolarizing_error(0.01, 1)
error_2 = noise.depolarizing_error(0.1, 2)
noise_model.add_all_qubit_quantum_error(error_1, ['u', 'u1', 'u2', 'u3'])
noise_model.add_all_qubit_quantum_error(error_2, ['cx'])
readout_error = noise.ReadoutError([[0.9, 0.1], [0.1, 0.9]])
noise_model.add_all_qubit_readout_error(readout_error)
backend = Aer.get_backend('qasm_simulator')

fig, axs = plt.subplots(3, 1, figsize=(5, 12))

for idx, a in enumerate([11, 7, 13]):
    q = QuantumRegister(5, 'q')
    c = ClassicalRegister(3, 'c')
    shor = QuantumCircuit(q, c)
    circuit_aperiod15(shor, q, c, a)
    qc_transpile = transpile([shor], backend)
    job = backend.run(qc_transpile, noise_model=noise_model, shots=10000)
    result = job.result()
    counts = dict(result.get_counts())
    plot_histogram(counts, ax=axs[idx])
    axs[idx].set_title(f'Histogramme de probabilité pour x = {a}')
    axs[idx].set_xlabel('Résultat de mesure')
    axs[idx].set_ylabel('Count')

plt.tight_layout()
plt.show()
