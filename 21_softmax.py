import numpy as np

'''
Let's pretend we're looking at the output of the neural network or the activation of last layer.
We have 5 different numbers that represent 5 different nodes at the output layer
'''
a = np.random.rand(5)
print(a)
'''
First step is to exponentiate them
'''
exp_a = np.exp(a)
print(exp_a)
'''
Now answer should be equal to 1
'''
answer = exp_a / sum(exp_a)
print(answer)

