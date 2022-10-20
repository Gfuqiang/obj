import numpy as np

zeros_array = np.zeros((2, 2, 2, 2))
one_array = np.ones((2, 4), dtype=np.uint8)
random_array = np.random.random((3, 4))
kernel = np.ones((5, 5), dtype=np.float32)/25
print(kernel)