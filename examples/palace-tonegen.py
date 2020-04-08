#!/usr/bin/env python3
# Example for tone generator
# Copyright (C) 2020  Ngô Ngọc Đức Huy
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

from argparse import Action, ArgumentParser
from itertools import count, takewhile
from enum import auto, Enum
from math import sin
from sys import stderr
from time import sleep
from typing import Iterable

from palace import Buffer, Context, Device, Source

CHUNK_LEN: int = 12000
QUEUE_SIZE: int = 4
PERIOD: float = 0.01
WAVE_TYPES: Iterable[str] = ['SINE', 'SQUARE', 'SAWTOOTH',
                             'TRIANGLE', 'IMPULSE', 'WHITE_NOISE']


class WaveType(Enum):
    SINE = auto()
    SQUARE = auto()
    SAWTOOTH = auto()
    TRIANGLE = auto()
    IMPULSE = auto()
    WHITE_NOISE = auto()


class TypePrinter(Action):
    def __call__(self, parser: ArgumentParser, *args, **kwargs) -> None:
        print('Available waveform types:')
        for t in WAVE_TYPES:
            print(t)
        parser.exit()


def apply_sin(data: Iterable[float], g: float,
              srate: int, freq: int) -> None:
    samps_per_cycle: float = srate / freq
    for i in range(srate):
        data[i] += sin((i/samps_per_cycle) % 1 * 2 * pi) * g


def create_wave(type: WaveType, freq: int, srate: int) -> Buffer:
    seed = 42069
    data = [0] * srate
    buf = Buffer()


def play(device: Device, waveform: str = 'sine') -> None:
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--types', nargs=0, action=TypePrinter,
                        help='print available waveform types in this example')
    parser.add_argument('-w', '--waveform', nargs='+', help='audio files')
    parser.add_argument('-d', '--device', default='', help='device name')
    args = parser.parse_args()
    play(args.device, args.waveform)
