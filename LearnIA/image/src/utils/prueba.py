import numpy as np

x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]
y = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1]]

list = np.array([1, 2, 3])
validation_split = .2
num_samples = len(x)
num_train_samples = int((1 - validation_split)*num_samples)
train_x = x[:num_train_samples]
train_y = y[:num_train_samples]
val_x = x[num_train_samples:]
val_y = y[num_train_samples:]
train_data = (train_x, train_y)
val_data = (val_x, val_y)

print(list.shape)