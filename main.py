import numpy as np
import matplotlib.pyplot as plt

from holography import create_object, gaussian, off_axis_hologram
from masks import generate_random_masks, hadamard_patterns
from reconstruction import (
    ista_reconstruction,
    hadamard_reconstruction,
    nnls_reconstruction,
    reconstruct_off_axis_auto
)
from utils import show_results


def main():

    # -----------------------------
    # Parameters
    # -----------------------------
    size = 64
    dx = 0.5e-3
    wavelength = 0.857e-3
    wo = 0.0015
    z = 0.25
    angle = 25 * np.pi / 180
    M = 4000   # measurements for ISTA / NNLS

    # -----------------------------
    # Object + beam
    # -----------------------------
    obj = create_object(size)
    beam = gaussian(wo, z, size, dx, wavelength)
    O = obj * beam

    # -----------------------------
    # Hologram
    # -----------------------------
    holo = off_axis_hologram(O, wavelength, dx, angle, beam)
    holo = holo / np.max(holo)

    # =============================
    # 1. HADAMARD
    # =============================
    print("Hadamard reconstruction...")
    H = hadamard_patterns(size)
    holo_hadamard = hadamard_reconstruction(holo, H)

    # =============================
    # 2. ISTA
    # =============================
    print("ISTA reconstruction...")
    masks, A = generate_random_masks(size, M)
    y = np.array([np.sum(holo * m) for m in masks])
    y = y / np.max(y)

    holo_ista = ista_reconstruction(A, y, size)

    # =============================
    # 3. NNLS (smaller size recommended)
    # =============================
    print("NNLS reconstruction...")
    holo_nnls = nnls_reconstruction(A, y, size)

    # =============================
    # Recover object
    # =============================
    amp_h, _ = reconstruct_off_axis_auto(holo_hadamard)
    amp_i, _ = reconstruct_off_axis_auto(holo_ista)
    amp_n, _ = reconstruct_off_axis_auto(holo_nnls)

    # =============================
    # Show
    # =============================
    show_results(obj, holo, amp_h, amp_i, amp_n)


if __name__ == "__main__":
    main()
