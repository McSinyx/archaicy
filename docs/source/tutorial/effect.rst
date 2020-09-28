Adding an effect
================

.. currentmodule:: palace

This section will focus on how to add effects to the audio.

There are two set of audio effects supported by palace: :py:class:`ReverbEffect`
and :py:class:`ChorusEffect`.

Reverb effect
-------------

Reverb happens when a sound is reflected and then decay as the sound is absorbed
by the objects in the medium.  :py:class:`ReverbEffect` facilitates such effect.

Creating a reverb effect can be as simple as:

.. code-block:: python
   effect = ReverbEffect()
   source.sends[0].effect = effect

