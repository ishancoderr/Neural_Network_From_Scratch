import numpy as np

def sigmoid(x):
    return 1/(1*np.exp(-x))

def sigmoid_deravative(x):
    return x*(1-x)

training_inputs =np.array([[0,0,1],
                           [1,1,1],
                           [1,0,1],
                           [0,1,1]])

training_outputs =np.array([[0,1,1,0]]).T

np.random.seed(1)


synaptic_weights =2*np.random.random((3,1))-1

print("Random start synaptic weights:")
print(synaptic_weights)

for iteration in range(200):
    input_layer=training_inputs
    print(input_layer.T)
    outputs=sigmoid(np.dot(input_layer,synaptic_weights))
    error=training_outputs- outputs
    adjestment=error*sigmoid_deravative(outputs)
    print(adjestment)
    synaptic_weights=np.dot(input_layer.T,adjestment) + synaptic_weights


print("synaptic weights after training:")
print(synaptic_weights)
print("Output after training:")
print(outputs)