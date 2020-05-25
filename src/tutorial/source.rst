.. py:currentmodule:: palace

Source manipulation
===================

We have created a source in the last section.
As said previously, its properties can be manipulated
to create wanted effects.

Moving the source
-----------------

Changing :py:meth:`Source.position` is one of the most noticeable,
but first, we have to enable spatialization via :py:attr:`Source.spatialize`.

.. code-block:: python

   from time import sleep
   from palace import Device, Context, Source, decode

   filename = 'some_audio.ogg'
   with Device() as dev, Context(dev) as ctx:
       with Source() as src:
           src.spatialize = True

           dec = decode(filename)
           dec.play(12000, 4, src)
           while src.playing:
               sleep(0.025)
               ctx.update()

Now, we can set the position of the source in this virtual 3D space.
The position is a 3-tuple indicating the coordinate of the source.
For those who didn't know this yet: x is for left-right, y is for up-down,
and z is for back-forth.
For example, this will set the source above you:

.. code-block:: python
   src.position = 0, 1, 0

*Note*: for this too work, you have to have HRTF enabled.  You can check that
via :py:attr:`Device.current_hrtf`.

You can as well use a function to move the source automatically by writing
a function that generate positions.  A simple example is circular motion.

.. code-block:: python
   from itertools import takewhile, count
   def rotate(t):
       return sin(t), 0, -cos(t)
   ...
   for i in takewhile(src.playing, count(step=0.025)):
       src.position = rotate(i)
       ...

A more well-written example of this can be found on our `repository`_.

Pitch
-----

Modifying :py:attr:`pitch` changes the playing speed, effectively changing
pitch.  Pitch can be any positive number.

.. code-block:: python
   src.pitch = 7  # quite high pitch
   src.pitch = 0.4  # low pitch

Air absorption factor
---------------------

:py:attr:`Source.air_absorption_factor` simulates atmospheric high-frequency
air absorption. Higher values simulate foggy air and lower values simulate
drier air.

.. code-block:: python
   src.air_absorption_factor = 9  # very high humidity
   src.air_absorption_factor = 0  # by default: dry air

.. _repository: https://github.com/McSinyx/palace/blob/master/examples/palace-hrtf.py
