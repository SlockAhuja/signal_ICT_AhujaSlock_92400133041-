import numpy as np
from signal_ICT_AhujaSlock_92400133041.unitary_signals import unit_step, unit_impulse, ramp_signal
from signal_ICT_AhujaSlock_92400133041.trigonometric_signals import sine_wave, cosine_wave
from signal_ICT_AhujaSlock_92400133041.operations import time_shift, signal_addition, signal_multiplication

# Test unitary signals
step = unit_step(5)
impulse = unit_impulse(5)
ramp = ramp_signal(5)

# Test trigonometric signals
t = np.linspace(0, 1, 100)
sine = sine_wave(A=1, f=1, phi=0, t=t)
cosine = cosine_wave(A=1, f=1, phi=0, t=t)

# Test operations
shifted = time_shift(sine, 10)
added = signal_addition(step, ramp)
multiplied = signal_multiplication(sine, cosine)

print("Installation test successful! All functions executed without errors.")
