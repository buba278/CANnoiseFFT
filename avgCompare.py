import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_csv_data(file_path):
    """
    Reads CSV data from the oscilloscope.
    Assumes the CSV file has columns: second, Volt.
    """
    data = pd.read_csv(file_path)
    time = data['second'].values
    voltage = data['Volt'].values
    return time, voltage

def compute_frequency_spectrum(time, voltage):
    """
    Computes the frequency spectrum of the signal.
    """
    # Number of samples
    N = len(voltage)
    
    # Sampling interval (assuming uniform sampling)
    T = time[1] - time[0]
    
    # Compute the FFT
    fft_values = np.fft.fft(voltage)
    fft_freqs = np.fft.fftfreq(N, T)
    
    # Only keep the positive frequencies
    positive_freqs = fft_freqs[:N//2]
    positive_fft_values = 2.0/N * np.abs(fft_values[:N//2])
    
    return positive_freqs, positive_fft_values

def plot_average_spectrum(freqs, spectra, label):
    """
    Plots the average frequency spectrum.
    """
    average_spectrum = np.mean(spectra, axis=0)
    plt.plot(freqs, average_spectrum, label=label)

def main():
    # File paths
    files = {
        'Baseline': [
            'bench test sd card/baseline.csv'
        ],
        'glv': [
            'car testing flash/glv2.csv'
        ],
        'rtd': [
            'car testing flash/rtd1.csv',
            'car testing flash/rtd2.csv',
            'car testing flash/rtd3.csv',
            'car testing flash/rtd4.csv'
        ],
        'TSactive': [
            'car testing flash/TSactive1.csv',
            'car testing flash/TSactive2.csv',
            'car testing flash/TSactive3.csv',
            'car testing flash/TSactive4.csv',
            'car testing flash/TSactive5.csv',
            'car testing flash/TSactive6.csv',
            'car testing flash/TSactive7.csv'
        ]
    }
    
    plt.figure(figsize=(12, 6))
    
    for label, file_paths in files.items():
        all_spectra = []
        for file_path in file_paths:
            time, voltage = read_csv_data(file_path)
            freqs, spectrum = compute_frequency_spectrum(time, voltage)
            all_spectra.append(spectrum)
        plot_average_spectrum(freqs, all_spectra, label)
    
    plt.title('Average Frequency Spectrum Comparison')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
