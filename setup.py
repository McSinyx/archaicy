#!/usr/bin/env python3
from os import makedirs
from os.path import abspath, dirname, join
from subprocess import check_call
from sys import version_info

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

PYTHON_VERSION = '{}.{}.{}'.format(*version_info)
PARENT_DIR = dirname(abspath(__file__))
with open(join(PARENT_DIR, 'README.md')) as f: LONG_DESCRIPTION = f.read()


class cmake_ext(build_ext):
    """Build extension using CMake."""
    def run(self):
        """Use CMake to build the extension in build_lib directory."""
        makedirs(self.build_lib, exist_ok=True)
        check_call(['cmake', f'-DPYTHON_VERSION={PYTHON_VERSION}', PARENT_DIR],
                   cwd=self.build_lib)
        check_call(['cmake', '--build', '.'], cwd=self.build_lib)


setup(
    name='palace',
    version='0.0.3',
    description='Pythonic Audio Library and Codecs Environment',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/McSinyx/palace',
    author='Nguyễn Gia Phong',
    author_email='vn.mcsinyx@gmail.com',
    license='LGPLv3+',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C++',
        'Programming Language :: Cython',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Software Development :: Libraries',
        'Typing :: Typed'],
    keywords='openal alure hrtf',
    ext_modules=[Extension('palace', [])],  # compilation is handled by cmake
    cmdclass={'build_ext': cmake_ext},
    zip_safe=False)
