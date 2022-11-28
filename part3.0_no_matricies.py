# Pre-transition to vectors and matricies
inputs = [1, 2, 3, 2.5]

# Merging weights into one list
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

# Likewise, for the biases
biases = [2, 3, 0.5]

# The output calculation
layer_outputs = [] # Output of current layer

# Zip together weights and biases for each neuron and iterate over each pair, calculating the output
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of a given neuron
    for n_input, weight in zip(inputs, neuron_weights): # Zip together inputs and the neuron weights
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)