# Single_Pixel_holography
Single-pixel holography simulation with Hadamard, ISTA, and NNLS reconstruction
 Single Pixel Terahertz Holography (Python)


This project implements a simplified version of computational imaging pipeline for single-pixel holography using off-axis interference and structured illumination.
The system simulates a terahertz (~350 GHz) imaging setup and reconstructs an object from a hologram using different inverse methods.

- Motivation

At terahertz frequencies (~350 GHz), high-resolution detector arrays are expensive and technically challenging to realize.

Single-pixel imaging provides an efficient alternative by replacing spatial detector arrays with structured illumination and computational reconstruction. This enables high-resolution imaging using a single detector, making it especially useful in wavelength regimes where detector technology is limited.

-Methods

The pipeline consists of:

1. Off-axis holography
   - Interference between object and tilted reference beam
   - Generates spatial fringes encoding phase information

2. Single-pixel measurement
   - Structured masks (Hadamard / random)
   - Measurements obtained via inner product with hologram

3. Reconstruction algorithms
   - Hadamard reconstruction (deterministic, exact)
   - ISTA (Iterative Shrinkage Thresholding Algorithm)
   - NNLS(Non-negative least squares)

4. Object recovery
   - Fourier-domain filtering to extract sideband
   - Reconstruction of amplitude and phase
