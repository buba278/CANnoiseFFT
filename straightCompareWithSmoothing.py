import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def read_csv_data(file_path):
    """
    Reads CSV data from the oscilloscope.
    Assumes the CSV file has columns: second, Volt.
    """
    data = pd.read_csv(file_path)
    time = data['second'].values
    voltage = data['Volt'].values
    return time, voltage

def savitzky_golay_filter(data, window_size, poly_order):
    """
    Applies a Savitzky-Golay filter to the data.
    """
    return savgol_filter(data, window_size, poly_order)

def plot_frequency_spectrum(time, voltage, label):
    """
    Computes and plots the frequency spectrum of the signal.
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
    
    # Plot the frequency spectrum
    plt.plot(positive_freqs, positive_fft_values, label=label)

def main(window_size, poly_order):
    # File paths
    files = {
        'base no noise': 'tempfile/base.csv',
        '1.5Vpp 8Khz': 'tempfile/1.5.csv',
    }
    
    plt.figure(figsize=(12, 6))
    
    for label, file_path in files.items():
        time, voltage = read_csv_data(file_path)
        
        # Apply Savitzky-Golay filter
        voltage_smooth = savitzky_golay_filter(voltage, window_size, poly_order)
        
        plot_frequency_spectrum(time, voltage_smooth, label)
    
    plt.title('Frequency Spectrum Comparison')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # Adjust the window size and polynomial order to control smoothing
    window_size = 101  # Example: try different odd values like 21, 51, 101, etc.
    poly_order = 4  # Example: try different values like 2, 3, 4
    main(window_size, poly_order)
