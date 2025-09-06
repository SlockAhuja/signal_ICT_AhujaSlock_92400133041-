import numpy as np
import matplotlib.pyplot as plt
from signal_ICT_AhujaSlock_92400133041.unitary_signals import unit_step, unit_impulse, ramp_signal
from signal_ICT_AhujaSlock_92400133041.trigonometric_signals import sine_wave, cosine_wave
from signal_ICT_AhujaSlock_92400133041.operations import time_shift, signal_addition, signal_multiplication

# Generate and plot unit step and impulse signals
step_signal = unit_step(20)
impulse_signal = unit_impulse(20)

# Generate sine wave
t = np.linspace(0, 1, 500)
sine = sine_wave(A=2, f=5, phi=0, t=t)

# Time shift sine wave by +5 units (integer shift of samples)
shifted_sine = time_shift(sine, 5)

# Generate ramp signal
ramp = ramp_signal(20)

# Add unit step and ramp signal
added_signal = signal_addition(step_signal, ramp)

# Generate cosine wave
cosine = cosine_wave(A=2, f=5, phi=0, t=t)

# Multiply sine and cosine
multiplied_signal = signal_multiplication(sine, cosine)