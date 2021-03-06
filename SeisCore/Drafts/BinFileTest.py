from SeisCore.BinaryFile.BinaryFile import BinaryFile
from datetime import datetime, timedelta
from matplotlib import pyplot as plt


bin_data = BinaryFile()
bin_data.path = '/media/michael/Data/Projects/HydroFracturing/NorthDeposit' \
                '/Perforation/Binary/12_SigmaN001_2020-04-11_12-15-15.bin'
signal = bin_data.signals[1000:2000]
plt.plot(signal)
plt.show()
print(signal.shape[0])
signal = signal[
    (signal[:, 0] != 0) * (signal[:, 1] != 0) * (signal[:, 2] != 0)]
print(signal.shape[0])
print("")
exit(1)

bin_data.read_date_time_start = datetime(2019, 7, 28, 8, 0, 0) + timedelta(
    seconds=-1 * 3)
bin_data.read_date_time_stop = datetime(2019, 7, 28, 8, 0, 2)

print(bin_data.discrete_amount)
print(bin_data.check_correct())
exit(0)

bin_data.read_date_time_start = datetime(2019, 7, 28, 8, 0, 0) + timedelta(
    seconds=-1 * 3)
bin_data.read_date_time_stop = datetime(2019, 7, 28, 8, 0, 2)

signal = bin_data.signals[:, 0]

check_function(signal=signal, frequency=1000, order=3, long_window=0.5,
               short_window=0.05)

# sfa=sl_filter_a(signal,100,1,1,0.05)
# sfb=sl_filter_b(signal,100,1,1,0.05)
#
# print(np.max(np.abs(sfa-sfb)))
#
#
# print(bin_data.datetime_start, bin_data.datetime_stop)
# print(bin_data.longitude, bin_data.latitude)
# print(bin_data.signals.shape)
#
#

# bin_data.data_type='HydroFrac'
# bin_data.resample_frequency=250
# bin_data.use_avg_values=True
# signal=bin_data.signals
# print(signal[:20,2])
# print('Ok')
