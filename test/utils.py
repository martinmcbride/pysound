import numpy as np

def compare_buffers(a, b):
    """
    Check if two buffers are equal to within a tolerance. Throw ValueError if not.
    """
    if len(a) != len(b):
        raise ValueError(f"Buffers have different lengths {len(a)} nd {len(b)}")
    if not np.allclose(a, b):
        raise ValueError(f"Buffers are different")
