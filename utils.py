import matplotlib.pyplot as plt

def show_results(obj, holo, hadamard, ista, nnls):

    plt.figure(figsize=(12,4))

    plt.subplot(1,5,1)
    plt.title("Object")
    plt.imshow(obj, cmap='gray')

    plt.subplot(1,5,2)
    plt.title("Hologram")
    plt.imshow(holo, cmap='gray')

    plt.subplot(1,5,3)
    plt.title("Hadamard")
    plt.imshow(hadamard, cmap='gray')

    plt.subplot(1,5,4)
    plt.title("ISTA")
    plt.imshow(ista, cmap='gray')

    plt.subplot(1,5,5)
    plt.title("NNLS")
    plt.imshow(nnls, cmap='gray')

    plt.tight_layout()
    plt.show()
