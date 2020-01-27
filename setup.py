#!/usr/bin/env python3
from distutils.file_util import copy_file
from distutils.dir_util import mkpath
from glob import iglob
from itertools import chain
from os.path import abspath, dirname, join
from platform import python_version
from subprocess import check_call

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


class cmake_ext(build_ext):
    """Build extension using CMake."""
    def run(self) -> None:
        """Use CMake to build the extension in build_temp
        and copy it to build_lib for installation.
        """
        # Use CMake to build the extension in build_temp
        mkpath(self.build_temp)
        print('generating build system in', self.build_temp)
        check_call(['cmake', f'-DPYTHON_VERSION={python_version()}',
                    f'-S{dirname(abspath(__file__))}', f'-B{self.build_temp}'])
        print('building extension in', self.build_temp)
        check_call(['cmake', '--build', self.build_temp])

        # Copy the extension to build_lib for installation
        mkpath(self.build_lib)
        for ext in chain.from_iterable(iglob(join(self.build_temp, libpattern))
                                       for libpattern in ('*.so', '*.dll')):
            copy_file(ext, self.build_lib)


# Compilation is handled by CMake, thus no source file is passed to Extension.
setup(ext_modules=[Extension('palace', [])], cmdclass={'build_ext': cmake_ext})
