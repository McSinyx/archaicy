#!/usr/bin/env python3
# Sample for tone generator
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
from array import array
from math import pi, sin
from random import random
from typing import Iterable, Tuple

from palace import Buffer, Context, BaseDecoder, Device

from numpy import linspace
from numpy.random import random
from scipy.signal import sawtooth, square, unit_impulse

WAVEFORMS = {'sine': sin,
             'square': square,
             'sawtooth': sawtooth,
             'triangle': lambda time: return sawtooth(time, 0.5),
             'impulse': lambda time: return unit_impulse(time * frequency % 1),
             'white noise': random}


class ToneGenerator(BaseDecoder):
    def __init__(self, waveform: str, duration: int, frequency: int):
        self.func = lambda frame: WAVEFORMS[waveform](frame/self.frequency,
                                                      frequency)
        self.duration = duration

    @BaseDecoder.frequency.getter
    def frequency(self) -> int: return 44100

    @BaseDecoder.channel_config.getter
    def channel_config(self) -> str:
        return 'Mono'

    @BaseDecoder.sample_type.getter
    def sample_type(self) -> str:
        return 'Float32'

    @BaseDecoder.length.getter
    def length(self) -> int: return self.duration

    def seek(self, pos: int) -> bool: return False

    @BaseDecoder.loop_points.getter
    def loop_points(self) -> Tuple[int, int]: return 0, 0

    def read(self, count: int) -> bytes:
        stop = min(self.start + count, self.length)
        data = array('f', map(self.func, range(self.start, stop)))
        self.start = stop
        return data.tobytes()


class TypePrinter(Action):
    def __call__(self, parser: ArgumentParser, *args, **kwargs) -> None:
        print('Available waveform types:', *WAVEFORMS, sep='\n')
        parser.exit()


def play(device: str, waveform: str, duration: int, frequency: int) -> None:
    with Device(device) as dev, Context(dev):
        dec = ToneGenerator(waveform, duration, frequency)
        with Buffer.from_decoder(dec, 'tonegen') as buf, buf.play() as src:
            _ = src


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--types', nargs=0, action=TypePrinter,
                        help='print available waveform types in this example')
    parser.add_argument('-w', '--waveform', default='SINE', nargs=1,
                        help='waveform to be generated')
    parser.add_argument('-d', '--device', default='', help='device name')
    parser.add_argument('-l', '--duration', default=30, type=int,
                        help='duration, in second')
    args = parser.parse_args()
    play(args.device, args.waveform, args.duration)
