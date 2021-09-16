# Author:  Martin McBride
# Created: 2021-09-12
# Copyright (C) 2021, Martin McBride
# License: MIT

from pysound.buffer import BufferParams

# BufferParams is immutable

# Create a default BufferParams
params1 = BufferParams()
print("params1", params1.get_length(), params1.get_sample_rate())

# Create BufferParams with custom length and sample rate
params2 = BufferParams(length=1000, sample_rate=5000)
print("params2", params2.get_length(), params2.get_sample_rate())

# Create BufferParams based on params2 with modified length
params3 = params2.with_length(2000)
print("params3", params3.get_length(), params3.get_sample_rate())

# Create BufferParams based on params2 with modified duration
# Duration fo 2s with sample rate of 5000 creates a buffer of length 10000
params4 = params2.with_duration(2)
print("params4", params4.get_length(), params4.get_sample_rate())

# Create BufferParams based on params2 with modified sample rate
params5 = params2.with_sample_rate(3000)
print("params5", params5.get_length(), params5.get_sample_rate())

