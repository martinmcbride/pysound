# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Constant value

import numpy as np

def constant(params, value):
    buffer = np.zeros(params.size)
    buffer.fill(value)
    while True:
        yield buffer