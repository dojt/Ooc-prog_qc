##########################
#######Zomok Dragon#######
##########################

from qiskit import QuantumCircuit
from qiskit import BasicAer, execute

def make_ghz3(shots, device):
    # Make a quantum circuit for the GHZ state.
    qubits_number = 3
    qc = QuantumCircuit(qubits_number, qubits_number)

    # Create a GHZ state
    qc.h(0)
    for i in range(qubits_number-1):
        qc.cx(i, i+1)

    # Insert a barrier before measurement
    qc.barrier()
    
    # Measure all of the qubits in the standard basis
    for i in range(qubits_number):
        qc.measure(i, i)

    sim_backend = BasicAer.get_backend(device)
    job = execute(qc, sim_backend, shots=shots)
    return job.result()

