import numpy as np

def generate_sine_wave(frequency, amplitude, duration, sample_rate=1000):
    """Generates a sine wave signal."""
    if duration < 0:
        return np.array([]), np.array([])
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    """ returns time array and sine wave values"""
    return t, y 

def test_generate_sine_wave():
    """Tests for the generate_sine_wave function."""
    t, y = generate_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0
    """ Check peak amplitude """

    t, y = generate_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)
    """ Check frequency """

    t, y = generate_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0
    """ Check zero duration """

    t, y = generate_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)
    """ Check zero amplitude """
    

def step_function(t, step_time, low_value=0, high_value=1):
    """Generates a step function signal."""
    y = np.where(t < step_time, low_value, high_value)
    """ returns time array and step function values """
    return t, y

def test_step_function():
    """Tests for the step_function."""
    t = np.linspace(0, 1, 100)
    t_out, y = step_function(t, 0.5)
    assert len(t_out) == 100
    assert y[0] == 0
    assert y[-1] == 1
    assert y[49] == 0
    assert y[50] == 1
    """ Check custom low and high values """

    t_out, y = step_function(t, 0.2, low_value=-1, high_value=2)
    assert y[19] == -1
    assert y[20] == 2
    """ Check step at boundaries """
