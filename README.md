# palace
Palace is a Python 3D audio API wrapping around [alure].
To quote alure's README,

> It uses OpenAL for audio rendering, and provides common higher-level features
> such as file loading and decoding, buffer caching, background streaming,
> and source management for virtually unlimited sound source handles.

## Features
In some sense, what palace aimes to be to [OpenAL Soft] is what [ModernGL]
is to OpenGL (except that all the heavy-lifting are taken are by alure):

* 3D sound rendering
* Environmental audio effects: reverb, atmospheric air absorption,
  sound occlusion and obstruction
* Binaural (HRTF) rendering
* Out-of-the-box audio decoding of FLAC, MP3, Ogg Vorbis, Opus, WAV, AIFF, etc.
* Modern Pythonic API: snake_case, `@property`, `with` context manager,
  type annotation

## Installation
### Prerequisites
Palace requires Python 3.6+ for runtime and [pip] for installation.

### Via PyPI
Palace can be install from the [Python Package Index][PyPI] via simply

    pip install palace

Wheel distributions are built exclusively for amd64.  Currently, only GNU/Linux
is properly supported.  If you want to help packaging for Windows and macOS,
see [GH-1] and [GH-63] respectively on our issues tracker on GitHub.

### From source
Aside from the build dependencies listed in `pyproject.toml`, one will
additionally need compatible Python headers, [alure], a C++14 compiler,
[CMake] 2.6+ (and probably `git` for fetching the source).
Palace can then be compiled and installed by running

    pip install git+https://github.com/McSinyx/palace

## Usage
One may start with the `examples` for sample usage of palace.
For further information, Python's `help` is your friend and
the API is also available for [online reference][API].

## License and Credits
Palace is free software: you can redistribute it and/or modify it
under the terms of the [GNU Lesser General Public License][LGPLv3+]
as published by the Free Software Foundation, either version 3
of the License, or (at your option) any later version.

Credits to the works bundled with palace can be found in our user
documentation.

[alure]: https://github.com/kcat/alure
[OpenAL Soft]: https://kcat.strangesoft.net/openal.html
[ModernGL]: https://github.com/moderngl/moderngl
[Cython]: https://cython.org/
[pip]: https://pip.pypa.io/en/latest/
[PyPI]: https://pypi.org/project/palace/
[GH-1]: https://github.com/McSinyx/palace/issues/1
[GH-63]: https://github.com/McSinyx/palace/issues/63
[CMake]: https://cmake.org/
[API]: https://mcsinyx.github.io/palace/html/reference.html
[LGPLv3+]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[Vorbis]: https://xiph.org/vorbis/
[Opus]: http://opus-codec.org/
[libsndfile]: http://www.mega-nerd.com/libsndfile/
