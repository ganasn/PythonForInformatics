#Handling overflow error
import math
signal_power = 9
#noise_power = 10.0
noise_power = 10
#ratio = signal_power/noise_power
ratio = signal_power/float(noise_power)
print ratio
decibels = 10 * math.log10(ratio)
print decibels