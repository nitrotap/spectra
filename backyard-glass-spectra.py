import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to convert wavelength to RGB
def wavelength_to_rgb(wavelength):
    gamma = 0.8
    intensity_max = 255
    factor = 0.0
    R = G = B = 0

    if 380 <= wavelength < 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength < 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength < 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength < 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength < 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 780:
        R = 1.0
        G = 0.0
        B = 0.0
    else:
        R = G = B = 0.0

    # Let the intensity fall off near the vision limits
    if 380 <= wavelength < 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength < 645:
        factor = 1.0
    elif 645 <= wavelength <= 780:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 645)
    else:
        factor = 0.0

    R = int(intensity_max * ((R * factor) ** gamma))
    G = int(intensity_max * ((G * factor) ** gamma))
    B = int(intensity_max * ((B * factor) ** gamma))

    return (R / 255.0, G / 255.0, B / 255.0)

# Plotting individual spectra for each historical glass additive
def plot_emission_spectrum(element, peak_wavelengths, filename):
    fig, ax = plt.subplots(figsize=(10, 2))
    for wl in peak_wavelengths:
        color = wavelength_to_rgb(wl)
        rect = patches.Rectangle((wl, 0), 10, 1, linewidth=1, edgecolor='none', facecolor=color)
        ax.add_patch(rect)
    ax.set_xlim(380, 780)
    ax.set_ylim(0, 1)
    ax.set_xticks([380, 440, 490, 510, 580, 645, 780])
    ax.set_yticks([])
    ax.set_xlabel('Wavelength (nm)')
    ax.set_title(f'Emission Spectrum of {element}')

# Plotting spectra for each element
elements = {
    'Iron (Fe)': [425, 900],
    'Cobalt (Co)': [590, 620],
    'Chromium (Cr)': [570, 630],
    'Manganese (Mn)': [400],
    'Selenium (Se)': [500, 650],
    'Cadmium (Cd)': [480, 650],
    'Uranium (U)': [520, 580],
    'Gold (Au)': [540, 650]
}

# Generate images for each element
for element, peaks in elements.items():
    plot_emission_spectrum(element, peaks, element.replace(' ', '_').lower())
