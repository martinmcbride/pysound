# pysound

NOTE - currently undergoing a fairly major re-write to improve overall design. Existing references and tutorials are out of date.

pysound is a pure Python library for creating digital sound and music.

Features include:

* Based on a sound unit architecture.
* Covers every stage of sound creation:
  * Basic sound processors: oscillators, envelopes, filters, etc.
  * Instrument or effect design.
  * Mixing and sequencing.
  * Production.
* However, it doesn't have to do everything. Sounds can be interchanged with other systems at any stage in the process.
* It is extremely easy to write your own units in Python.
* Extra processes, for example computer composing, automated mixing etc can be implemented in Python.
* Your complete song or sound project will be written as a pure python program.

PySound uses numpy arrays to store and process sound. This allows for efficient processing, and also allows other libraries, for example SciPy, to be integrated easily.

