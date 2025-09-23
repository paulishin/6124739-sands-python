import os
os.chdir("C:\\Users\\shinp\\Documents\\unif\\python\\6124739_sands_python")

from signals import generate_sine_wave
wave = generate_sine_wave(5, 2, 100)
print(wave[:10])