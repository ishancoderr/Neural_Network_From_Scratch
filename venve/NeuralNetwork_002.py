import numpy as np

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)
        self.synaptic_weights=2*np.random.random((3,1))-1

    def sigmoid(self,x):
        return 1/(1*np.exp(-x))

    def sigmoid_deravative(x):
        return x*(1-x)

    def train(self,training_inputs,training_outputs,traning_iterarions):
        for iteration in range(traning_iterarions):
            output=self.think(training_inputes)
            error=training_outputs-output
            adjestment =np.dot(training_inputs.T,error*self.sigmoid_deravative(output))
            self.synaptic_weights=adjestment

    def think(self,inputs):
        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_weights))

        return output


if __name__ == '__main__':
    neuralNetwork=NeuralNetwork()
    print("Random synaptic weights")

    training_inputs= np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])

    training_outputs = np.array([[0, 1, 1, 0]]).T
    traning_iterarions=1000

    NeuralNetwork.train(training_inputs,training_outputs,traning_iterarions)

    print("synaptic weights after training:")
    print(neuralNetwork.synaptic_weights)

    A = str(input("input 1:"))
    B = str(input("input 2:"))
    C = str(input("input 3:"))

    print("New input data=",A,B,C)
    print("output data:")
    print(NeuralNetwork.think(np.array([A,B,C])))

