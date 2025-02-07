import random
# from micrograd_andrej.engine import Value
from engine import Value


class Module:

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []
    

class Neuron(Module):
    def __init__(self, nin):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1,1))
        # self.b  = Value(0.0)

    def __call__(self, x):
        """
        This does w*x + b

        how __call__ works
        => x = [2.0, 3.0]
           n = Neuron(2)
           n(x) --> python uses __call__ here
        """

        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        return out
    
    def parameters(self):
        return self.w + [self.b] # Store parameters which will be updated between backprop and forward pass
    
class Layer(Module):
    def __init__(self, nin, nout):
        # nout is how many neurons you want in the layer
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        outs = [n(x) for n in self.neurons] # value of the neuron after wi*xi + b is n(x) where n is a neuron in self.neurons
        return outs[0] if len(outs)==1 else outs
    
    def parameters(self):
        params = []

        for neuron in self.neurons:
            ps = neuron.parameters()
            params.extend(ps)

        return params
    
        # OR you could do => return [p for neuron in self.neurons for p in neuron.paramters()]

class MLP(Module):
    def __init__(self, nin, nouts):
        """Multi Layer Perceptron"""

        """
        nin (int) => no. of input neurons (These are the first layer neurons as we saw in the neuron and the Layer class)
        nouts (list) => Here we take a list of layers, in Layer class, we had just a single layer
        """

        """
        so lets say that we have 2 neurons in the first layer and we have 3 more layers each of size 4,4,1
        so,
        nin = 2
        nouts = [4, 4, 1]
        So, to also include the first layer in the stack of all layers, we do 
        ==> sz = [nin] + nouts
        """
        sz = [nin] + nouts

        """
        Now we create a list of layers and store it in self.layers
        """ 
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x) # here we take x (values of prev layer neurons) and return a new x which is the values of the current layer neurons
        return x
    
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]
        
