import numpy as np
from signal_ICT_AhujaSlock_92400133041 import unit_step, sine_wave

step = unit_step(10)
t = np.linspace(0, 1, 500)
sine = sine_wave(2, 5, 0, t)

print(step[:5], sine[:5])
