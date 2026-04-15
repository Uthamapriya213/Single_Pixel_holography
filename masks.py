import numpy as np
from scipy.linalg import hadamard


def generate_random_masks(size, M):
    masks = np.random.choice([-1, 1], (M, size, size))
    A = masks.reshape(M, size*size)
    A = A / np.linalg.norm(A, axis=1, keepdims=True)
    return masks, A


def hadamard_patterns(size):
    N = size * size
    return hadamard(N)
