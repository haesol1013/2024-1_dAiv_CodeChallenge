class Perceptron:
    def __init__(self, weights, bias):  # weights: list[int], bias: int
        self.weights = weights
        self.bias = bias

    def __call__(self, input_data):  # input_data: list[int]
        sum_ = sum([w*d for w, d in zip(self.weights, input_data)])
        return sum_ + self.bias


class Layer:
    def __init__(self, weights, biases):  # weights: list[list[int]], biases: list[int]
        self.perceptrons = [Perceptron(weight, bias) for weight, bias in zip(weights, biases)]

    def __call__(self, input_data):  # input_data: list[int]
        output = []
        for idx, perceptron in enumerate(self.perceptrons):
            output.append(perceptron(input_data[idx]))
        return output


class MLP:
    def __init__(self, weights, biases):  # weights: list[list[list[int]]], biases: list[list[int]]
        self.layer1 = Layer(weights[0], biases[0])
        self.layer2 = Layer(weights[1], biases[1])

    def __call__(self, tensor):
        hidden = self.layer1(tensor)
        out = self.layer2([hidden])
        return out


input_size, hidden_size, repeat = map(int, input().split(" "))

hidden_data = [map(int, input().split(" ")) for _ in range(hidden_size)]
hidden_weights = []
hidden_biases = []
input_indexes = []
for data in hidden_data:
    length, *others = data
    hidden_biases.append(others.pop())
    input_indexes.append(others[:length])
    hidden_weights.append(others[length:])

output_data = [int(d) for d in input().split(" ")]
output_bias = [output_data.pop()]
output_weights = [output_data]


def preprocess(d):
    return [[d[i-1] for i in idx] for idx in input_indexes]


inputs = map(preprocess, [[int(d) for d in input().split(" ")] for _ in range(repeat)])
model = MLP(weights=[hidden_weights, output_weights], biases=[hidden_biases, output_bias])

for data_ in inputs:
    output = model(data_)
    print(output[0])
