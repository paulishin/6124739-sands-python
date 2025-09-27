import numpy as np
import matplotlib.pyplot as plt

f = 3
om = 2 * np.pi * f
t = np.linspace(0, 2, 1000) 

cos_wave = np.cos(om * t)

shift = 0.25
shift_cos = np.cos(om * (t - shift))

plt.figure()
plt.plot(t, cos_wave, label="cos_wave")
plt.plot(t, shift_cos, label="shift_cos")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.show()