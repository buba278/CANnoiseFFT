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

def main():
    # File paths
    files = {
        'base no noise': 'tempfile/base.csv',
        # '.24': 'tempfile/240.csv',
        # '.5': 'tempfile/500.csv',
        # '1': 'tempfile/1.csv',
        # '1.5Vpp 8Khz': 'tempfile/1.5.csv',

        # '100mVpp 8Khz just noise': 'tempfile/arb8khzNoise.csv',

        # 'ARB 8kHz 3Vpp': 'bench test sd card/arb8kHz3Vpp.csv',
        # 'ARB 2Vpp': 'bench test sd card/arb2Vpp.csv',
        # 'ARB 3Vpp': 'bench test sd card/arb3Vpp.csv',
        # 'ARB 4Vpp': 'bench test sd card/arb4Vpp.csv'

        # "glv2":'car testing flash/glv2.csv',

        # "rtd1":'car testing flash/rtd1.csv',
        # "rtd2":'car testing flash/rtd2.csv',
        # "rtd3":'car testing flash/rtd3.csv',
        # "rtd4":'car testing flash/rtd4.csv',

        # "TSactive1":'car testing flash/TSactive1.csv',
        # "TSactive2":'car testing flash/TSactive2.csv',
        # "TSactive3":'car testing flash/TSactive3.csv',
        # "TSactive4":'car testing flash/TSactive4.csv',
        # "TSactive5":'car testing flash/TSactive5.csv',
        # "TSactive6":'car testing flash/TSactive6.csv',
        # "TSactive7":'car testing flash/TSactive7.csv'
    }
    
    plt.figure(figsize=(12, 6))
    
    for label, file_path in files.items():
        time, voltage = read_csv_data(file_path)
        plot_frequency_spectrum(time, voltage, label)
    
    plt.title('Frequency Spectrum Comparison')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
