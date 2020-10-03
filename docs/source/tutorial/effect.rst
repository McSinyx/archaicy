Adding an effect
================

.. currentmodule:: palace

This section will focus on how to add effects to the audio.

There are two set of audio effects supported by palace: :py:class:`ReverbEffect`
and :py:class:`ChorusEffect`.

Reverb Effect
-------------

Reverb happens when a sound is reflected and then decay as the sound is absorbed
by the objects in the medium.  :py:class:`ReverbEffect` facilitates such effect.

Creating a reverb effect can be as simple as:

.. code-block:: python

   source.sends[0].effect = ReverbEffect()

:py:attr:`Source.sends` is a collection of send path signals, each of which
contains `effects` and `filter` that describes it.  Here we are only concerned
about the former.

The above code would yield a *generic* reverb effect by default.
There are several other presets that you can use, which are listed
by :py:data:`reverb_preset_names`.  To use these preset, you can simply provide
the preset effect name as the first parameter for the constructor.  For example,
to use `PIPE_LARGE` preset effect, you can initialize the effect like below:

.. code-block:: python

   effect = ReverbEffect('PIPE_LARGE')

These effects can be modified via their attributes.

.. code-block:: python

   effect.gain = 0.4
   effect.diffusion = 0.65
   late_reverb_pan = 0.2, 0.1, 0.3

The list of these attributes and their constraints can be found
in the documentation of :py:class:`ReverbEffect`.

Chorus Effect
-------------

:py:class:`ChorusEffect` does not have preset effects like
:py:class:`ReverbEffect`, so you would have to initialize the effect attributes
on creation.

There are five parameters to initialize the effect, respectively: waveform,
phase, depth, feedback, and delay.

.. code-block:: python

   source.sends[0].effect = ChorusEffect('sine', 20, 0.4, 0.5, 0.008)

For the constraints of these parameters, please refer to the documentation.

Destroy the effects
-------------------

Like other objects in palace, effects must be destroyed after it has its jobs
done with `__exit__()`.  If you use `with` syntax (you should) as mentioned in
previous tutorials, the method will be called when you exit the `with` block.

