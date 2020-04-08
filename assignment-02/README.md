# Assignment # 2

Using the state vector simulator and the functions for plotting Bloch vectors, write Python code for visualizing single qubit gates. You might want to try to have an animation of sorts. For that, check the object returned by plot_bloch_multivector() -- it is a Matplotlib figure (https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.figure.Figure.html).

Using your code, prepare two visualizations or animations to present to the other groups.  For your two visualizations, pick two gates out of the following list of five:

1. One parameter: U1, Rx, Ry, Rz
1. Two parameters: U2
1. Three parameters: U3

Note that these gates have parameters, and your visualization should help the other groups (and yourself) understand what the gate does, when the values of the parameters vary.

Pay attention to the state from which you start: Often, |0⟩ is not a good starting point, because it doesn't change with changing the parameter (in other words, it's an eigenvector of the unitary operator). Consider several states to pick a good one.

Get used to working with the Qiskit API documentation for the figuring out how to use the gates. (E.g., https://qiskit.org/documentation/stubs/qiskit.circuit.QuantumCircuit.u3.html)

### Submission
The procedure for submitting your homework is the same as before. (Fork and pull request; create a sub-folder of this folder for your stuff.)

### Smooth visualizations with fixed parameters

IBM has beautiful visualizations of some of the gates here:
https://quantum-computing.ibm.com/docs/circ-comp/q-gates

But there, the parameters are fixed, e.g., U3(π/2,π/2,π/2) or so.
