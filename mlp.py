import numpy as np
from sklearn.datasets import fetch_openml

mnist = fetch_openml("mnist_784", version=1, as_frame=False)

X = mnist.data
y = mnist.target.astype(int)

X = X.astype(np.float32) / 255.0

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    x -= np.max(x, axis=1, keepdims=True)
    x = np.exp(x)
    return x / np.sum(x, axis =1, keepdims=True)

# def test(x):
#     print(x.shape)
#     print(x.ndim)
#     print(x.dtype.name)
#     print(x.itemsize)
#     print(x.size)
#     print(type(x))

class layer:
    def __init__(self, input_size, output_size):
        self.w = np.random.randn(input_size, output_size).astype(np.float32)
        self.b = np.zeros(output_size, dtype=np.float32)

    def mul(self, input):
        return input @ self.w + self.b

    def forward(self):
        return 0

    def backward(self):
        return 0

l1 = layer(X.shape[1], 128)
l2 = layer(128, 128)
l3 = layer(128, 10)
 
print(softmax(l3.mul(relu(l2.mul(relu(l1.mul(X)))))))