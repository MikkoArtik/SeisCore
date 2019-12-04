import numpy as np
from scipy.fftpack import rfft, irfft, rfftfreq


def band_pass_filter(signal, frequency, f_min, f_max):
    """
    Bandpass filtering
    :param signal: input 1-D array of signal
    :param frequency: signal frequency
    :param f_min: minimal filtering frequency
    :param f_max: maximal filtering frequency
    :return: output 1-D array of signal
    """
    # построение частотного ряда
    frequency_array = rfftfreq(n=signal.shape[0], d=1.0 / frequency)
    # прямое преобразование Фурье
    f_signal = rfft(signal)
    # зануление амплитуд, частоты которых меньше f_min
    f_signal[((frequency_array < f_min)+(frequency_array > f_max))] = 0
    # зануление амплитуд, частоты которых больше f_max
    # обратное преобразование Фурье (получится отфильтрованный сигнал)
    filtered_signal = irfft(f_signal)
    return filtered_signal


def marmett(signal, order):
    """
    Marmett filter
    :param signal: input 1-D array of signal
    :param order: filter order
    :return: output 1-D array of signal
    """
    for i in range(order):
        j = 1
        recalc = signal.copy()
        while j < signal.shape[0] - 1:
            recalc[j] = (signal[j - 1] + signal[j + 1]) / 4 + signal[j] / 2
            j += 1
        recalc[0] = (signal[0] + signal[1]) / 2
        recalc[-1] = (signal[-1] + signal[-2]) / 2
        signal = recalc.copy()
    return signal


def sl_filter(signal, frequency, order=3, short_window=0.1, long_window=1):
    """
    Function for sta/lta filtration
    :param signal: one-dimension array os signal
    :param frequency: signal frequency
    :param order: filter order
    :param long_window: long window size (seconds)
    :param short_window: short window size (seconds)
    :return: filtered signal (one-dimension array)
    """
    long_window = int(frequency * long_window)
    short_window = int(frequency * short_window)

    for j in range(order):
        left_lim = j * long_window
        coeffs = np.zeros_like(signal)
        lta_sum = 0
        sta_sum = 0
        for i in range(left_lim + long_window,
                       signal.shape[0] - short_window):
            lta_window = signal[i - long_window:i]
            sta_window = signal[i - short_window:i]
            if i == 0:
                lta_sum = np.sum(np.abs(lta_window))
                sta_sum = np.sum(np.abs(sta_window))
            else:
                lta_sum = lta_sum - np.abs(signal[i - long_window - 1]) + \
                          np.abs(signal[i - 1])
                sta_sum = sta_sum - np.abs(signal[i - short_window - 1]) + \
                          np.abs(signal[i - 1])

            lta = lta_sum / long_window
            sta = sta_sum / short_window

            if lta == 0:
                val = 0
            else:
                val = sta / lta
            coeffs[i] = val

        coeffs = (coeffs - np.min(coeffs)) / (np.max(coeffs) - np.min(coeffs))
        signal = signal * coeffs
    return signal
