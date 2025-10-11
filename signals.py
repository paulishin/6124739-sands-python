import numpy as np
def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, y 

def test_generate_sine_wave():
    t, y = generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = generate_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = generate_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = generate_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)
    
