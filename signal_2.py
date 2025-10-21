import numpy as np 

def step_function(t, step_time, low_value=0, high_value=1):
    """Generates a step function signal."""
    y = np.where(t < step_time, low_value, high_value)
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

    t_out, y = step_function(t, 0.2, low_value=-1, high_value=2)
    assert y[19] == -1
    assert y[20] == 2