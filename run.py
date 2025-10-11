import os
os.chdir("C:\\Users\\shinp\\Documents\\unif\\python\\6124739-sands-python")

from signals import generate_sine_wave
t, y = generate_sine_wave(1, 2, 1)
print(t[:5], y[:5]) 