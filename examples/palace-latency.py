#!/usr/bin/env python3
# Example for latency checking
# Copyright (C) 2020 Ngô Ngọc Đức Huy
#
# This file is part of palace.
#
# palace is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# palace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with palace.  If not, see <https://www.gnu.org/licenses/>.

from argparse import ArgumentParser
from sys import exit

from palace import (
    Buffer, Context, Device, Source,
    query_extension)


def load_proc(T, x):
    """Load the function pointers."""
    pass


def load_sound(filename: str) -> Buffer:
    # Why is buffer an int? Why is everything int???
    # SNDFILE? SF_INFO? Where is that in palace?
    pass


def play(src: Source) -> None:
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('filename', help='audio files')
    parser.add_argument('-d', '--device', default='', help='device name')
    args = parser.parse_args()
    filename = args.filename
    with Device(args.device) as dev:
        # TODO: Something equivalent to InitAL
        if not query_extension('AL_SOFT_source_latency'):
            exit('Error: AL_SOFT_source_latency not supported')
            load_proc()  # TODO: implement that
            with Context(dev) as ctx, load_sound(args.filename) as Buffer, Source() as src:
                play()
                # TODO: Finish this
        
