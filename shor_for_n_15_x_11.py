# from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
# from qiskit_aer import Aer, noise
# from qiskit.circuit.library import QFT
# from qiskit.visualization import plot_histogram
# import numpy as np
# import matplotlib.pyplot as plt

# q = QuantumRegister(5, 'q')  
# c = ClassicalRegister(4, 'c')  
# circuit = QuantumCircuit(q, c)

# circuit.h(q[0:3])
# circuit.cx(q[2], q[3])
# circuit.cx(q[2], q[4])

# circuit.barrier()
# circuit.h(q[1])

# circuit.barrier()

# circuit.cp(np.pi / 2, q[1], q[0])
# circuit.barrier()

# circuit.h(q[0])
# circuit.barrier()

# circuit.cp(np.pi / 4, q[2], q[1])
# circuit.cp(np.pi / 2, q[0], q[2])

# circuit.barrier()

# circuit.measure(q[0:3], c[0:3])

# noise_model = noise.NoiseModel()
# error = noise.depolarizing_error(0.01, 1)  # single-qubit error
# noise_model.add_all_qubit_quantum_error(error, ['u1', 'u2', 'u3'])

# readout_error = noise.ReadoutError([[0.9, 0.1], [0.1, 0.9]])
# noise_model.add_all_qubit_readout_error(readout_error)

# simulator = Aer.get_backend('qasm_simulator')
# transpile_qc = transpile(circuit, simulator)
# job = simulator.run(transpile_qc, noise_model=noise_model, shots=10000)
# result = job.result()

# counts1 = result.get_counts()
# print("Measurement Results:", counts1)
# print("\nCircuit:")
# print(circuit.draw())

# plot_histogram(counts1).savefig("result_avec_bruitx11N15.png")
# plt.tight_layout()
# plt.savefig("result_avec_bruitx11N15.png")
# plt.show()

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.circuit.library import QFT
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

q = QuantumRegister(5, 'q')
c = ClassicalRegister(4, 'c')
circuit = QuantumCircuit(q, c)

circuit.h(q[0:3])
circuit.cx(q[2], q[3])
circuit.cx(q[2], q[4])

circuit.barrier()
circuit.h(q[1])

circuit.barrier()
circuit.cp(np.pi / 2, q[1], q[0])
circuit.barrier()
circuit.h(q[0])
circuit.barrier()
circuit.cp(np.pi / 4, q[2], q[1])
circuit.cp(np.pi / 2, q[0], q[2])
circuit.barrier()

circuit.measure(q[0:3], c[0:3])

simulator = Aer.get_backend('qasm_simulator')
transpile_qc = transpile(circuit, simulator)
job = simulator.run(transpile_qc, shots=10000)
result = job.result()

counts1 = result.get_counts()
print("Measurement Results:", counts1)
print("\nCircuit Diagram:")
print(circuit.draw())

keys = [f"{i:04b}" for i in range(16)]

counts1 = {key: counts1.get(key, 0) for key in keys}

plot_histogram(counts1).savefig("result_sans_bruitx11N15.png")
plt.tight_layout()
plt.savefig("result_sans_bruitx11N15.png")
plt.show()

