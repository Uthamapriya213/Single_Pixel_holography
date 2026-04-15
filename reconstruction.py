import numpy as np
from scipy.optimize import nnls


# ---------------- ISTA ----------------
def ista_reconstruction(A, y, size, lam=0.001, max_iter=200):

    x = np.zeros(A.shape[1])
    L = np.linalg.norm(A, ord=2)**2
    step = 1.0 / L

    for _ in range(max_iter):
        grad = A.T @ (A @ x - y)
        x = x - step * grad
        x = np.sign(x) * np.maximum(np.abs(x) - lam*step, 0)

    return x.reshape(size, size)


# ---------------- NNLS ----------------
def nnls_reconstruction(A, y, size):
    x, _ = nnls(A, y)
    return x.reshape(size, size)


# ---------------- HADAMARD ----------------
def hadamard_reconstruction(holo, H):

    x = holo.flatten()
    y = H @ x
    x_rec = H.T @ y / H.shape[0]

    return x_rec.reshape(holo.shape)


# ---------------- FFT RECON ----------------
def reconstruct_off_axis_auto(hologram, radius=20):

    H = np.fft.fftshift(np.fft.fft2(hologram))
    nx, ny = H.shape
    cx, cy = nx//2, ny//2

    H[cx-10:cx+10, cy-10:cy+10] = 0

    px, py = np.unravel_index(np.argmax(np.abs(H)), H.shape)

    mask = np.zeros_like(H)
    x, y = np.ogrid[:nx, :ny]
    mask[(x-px)**2 + (y-py)**2 < radius**2] = 1

    H_filtered = H * mask
    H_centered = np.roll(np.roll(H_filtered, cx-px, axis=0), cy-py, axis=1)

    field = np.fft.ifft2(H_centered)

    return np.abs(field), np.angle(field)
