import os
import matplotlib.pyplot as plt
os.chdir("C:\\Users\\shinp\\Documents\\unif\\python\\6124739-sands-python")


from signals import generate_sine_wave
t, y = generate_sine_wave(1, 2, 1)
print(y[:5]) 

shift = 0.25
t_shift = t + shift

plt.figure()
plt.plot(t, y, label="sin wave")
plt.plot(t_shift, y, label="shifted sin wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.show()


from signal_2 import step_function
t_step, y_step = step_function(t, 0.5)
shifted_t = t + shift
t_step_shifted, y_step_shifted = step_function(shifted_t, 0.5)

plt.figure()
plt.plot(t, y_step, label="step function")
plt.plot(t, y_step_shifted, label="shifted step function")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.legend()
plt.grid(True)
plt.show()

