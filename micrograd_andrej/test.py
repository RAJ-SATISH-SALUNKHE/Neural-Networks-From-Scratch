# from  micrograd_andrej.nn import Neuron, Layer, MLP
from nn import Neuron, Layer, MLP


def train(xs, ys, mlp, lr,passes, logging = True):
    ypred = [mlp(x) for x in xs]                                      # Predictions before tranining the neural network
    loss = sum([(ygt - yout)**2 for ygt, yout in zip(ys, ypred)])     # Loss before traning the neural network

    losses = []

    for i in range(passes):

        ypred = [mlp(x) for x in xs]
        loss = sum([(ygt - yout)**2 for ygt, yout in zip(ys, ypred)])

        """Zero Grad Operation"""
        for p in mlp.parameters():
            p.grad = 0

        loss.backward()

        for p in mlp.parameters():
            p.data += -lr * p.grad

        losses.append(loss.data)

        if i % 100 == 0 and logging:  
            print(f"Iteration {i}, Loss: {loss.data}")

    return mlp


if __name__ == '__main__':
    xs = [
        [2.0, 3.0, -1.0],
        [3.0, -1.0, 0.5],
        [0.5, 1.0, 1.0],
        [1.0, 1.0, -1.0]
    ]


    ys = [0.4, -1.0, -1.0, 0.27]

    # xs = [
    #     [2.0, 4.0, 6.0],
    #     [4.0, 6.0, 8.0],
    #     [6.0, 8.0, 10.0]
    # ]


    # ys = [8.0, 12.0, 18.0]

    # mlp = MLP(3, [4,4,1])
    mlp = MLP(3, [1])

    trained_mlp = train(xs, ys, mlp, lr = 0.01, passes=50000)

    # Predictions after traning
    ypred = [trained_mlp(x) for x in xs]

    print("Predicted Outputs : \n", [element.data for element in ypred])

    print("Expected Outputs: \n", [element for element in ys])

    # [3.0, -1.0, 0.5] - > -1

    # Testing 
    print("Test Result: ", trained_mlp([8.0, 10.0, 12.0]).data)


