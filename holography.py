import numpy as np

def create_object(size):
    obj = np.zeros((size, size))
    obj[size//2-10:size//2+10, size//2-10:size//2+10] = 1.0
    return obj


def gaussian(wo, z, size, dx, wavelength):
    k = 2*np.pi / wavelength
    x = np.arange(-size//2, size//2) * dx
    X, Y = np.meshgrid(x, x)
    r = np.sqrt(X**2 + Y**2)

    zr = np.pi * wo**2 / wavelength
    wz = wo * np.sqrt(1 + (z/zr)**2)
    R = z * (1 + (zr/z)**2)
    gouy = np.arctan(z/zr)

    return (wo/wz) * np.exp(-r**2 / wz**2) * np.exp(-1j*(k*z + k*(r**2/(2*R)) + gouy))


def off_axis_hologram(obj_field, wavelength, dx, angle, ref_amp):
    ny, nx = obj_field.shape

    x = np.arange(-nx//2, nx//2) * dx
    X, _ = np.meshgrid(x, x)

    k = 2*np.pi / wavelength
    R = ref_amp * np.exp(-1j * k * (X * np.sin(angle)))

    return np.abs(obj_field + R)**2
