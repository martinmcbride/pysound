# Author:  Martin McBride
# Created: 2016-01-08
# Copyright (C) 2016, Martin McBride
# License: MIT
# Website sympl.org/pysound
#
# Main pysound module

#Simple class to hold global parameters
class Params:
    def __init__(self, rate=11025, size=256, time=1.0):
        self.rate = rate #Samples per second
        self.size = size #Buffer size in samples
        self.time = time #Sound length in seconds
