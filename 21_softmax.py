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
Now sum of answer should be equal to 1
'''
answer = exp_a / exp_a.sum()
print(answer)
print(answer.sum())

'''
Lately we're going to work with multiple samples at the same time.
This mean we won't have 1-D array of length 5 but 2-D array of size (N,5)
'''
A = np.random.rand(100, 5)
print(A[:5])
exp_A = np.exp(A)
print(exp_A[:5])
answer_A = exp_A / exp_A.sum()
print(answer_A[:5])
print(answer_A.sum())