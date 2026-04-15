# Single_Pixel_holography
Single-pixel holography simulation with Hadamard, ISTA, and NNLS reconstruction
 
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
   - \[
      I = |O + R|^2
      \]

2. Single-pixel measurement
   - Structured masks (Hadamard / random)
   - Measurements obtained via inner product with hologram
   - \[
      y_i = \sum (I \cdot M_i)
      \]


3. Reconstruction algorithms
   - Hadamard reconstruction (deterministic, exact)
       - Uses orthogonal basis patterns
       - Differential measurement (positive/negative masks)
       - Fast and deterministic reconstruction
   - ISTA (Iterative Shrinkage Thresholding Algorithm)
       - Solves sparse inverse problem:
          \[
          \min_x \frac{1}{2}||Ax - y||^2 + \lambda ||x||_1
           \]

        - Uses gradient descent + soft-thresholding
   - NNLS(Non-negative least squares)
        - Enforces physical constraint (intensity ≥ 0)
        - Suitable for imaging problems

4. Object recovery
   After hologram reconstruction, the object is recovered using:

         - Fourier domain filtering
         - Sideband selection (off-axis holography)
         - Inverse FFT
5. Results

The pipeline demonstrates:

- Reconstruction of holograms using single-pixel measurements  
- Recovery of object amplitude via off-axis filtering  
- Comparison between Hadamard, ISTA, and NNLS methods



6. Key Insights

- Single-pixel imaging can be extended to holography  
- Reconstruction quality depends on:
  - number of measurements  
  - mask design  
  - regularization parameters  
- Iterative methods (ISTA) require careful tuning  
- Holographic reconstruction is more challenging than direct imaging due to interference encoding  



