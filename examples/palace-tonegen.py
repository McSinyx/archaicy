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
from numpy.random import random_sample
from scipy import signal

PERIOD: float = 0.025
WAVEFORMS = {'sine': sine,
             'square': square,
             'sawtooth': sawtooth,
             'triangle': triangle,
             'impulse': impulse,
             'white noise': white_noise}


class ToneGenerator(BaseDecoder):
    def __init__(self, waveform: str):
        self.func = lambda frame: WAVEFORMS[waveform](frame/self.frequency,
                                           self.frequency)

    @BaseDecoder.frequency.getter
    def frequency(self) -> int: return 44100

    @BaseDecoder.channel_config.getter
    def channel_config(self) -> str:
        return 'Mono'

    @BaseDecoder.sample_type.getter
    def sample_type(self) -> str:
        return 'Float32'

    @BaseDecoder.length.getter
    def length(self) -> int: return 0

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


def sine(time: int, sample_rate: int) -> Iterable[float]:
    """Generate sinusoidal signal."""
    t = linspace(0, time, time * sample_rate, endpoint=False)
    data = sin(t)
    return data


def square(time: int, sample_rate: int) -> Iterable[float]:
    """Generate square signal."""
    t = linspace(0, time, time * sample_rate, endpoint=False)
    data = signal.square(2 * pi * 5 * t)


def sawtooth(time: int, sample_rate: int) -> Iterable[float]:
    t = linspace(0, time, time * sample_rate, endpoint=False)
    data = signal.sawtooth(2 * pi * 5 * t)


def triangle(time: int, sample_rate: int) -> Iterable[float]:
    pass


def impulse(time: int, sample_rate: int) -> Iterable[float]:
    pass


def white_noise(time: int, sample_rate: int) -> Iterable[float]:
    return random_sample((1, time * sample_rate))
    


def play(device: str, waveform: str, duration: int) -> None:
    with Device(device) as dev, Context(dev):
        dec = ToneGenerator(waveform)
        _ = duration  # use it later
        buf = Buffer.from_decoder(dec, 'tonegen')
        buf.play()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--types', nargs=0, action=TypePrinter,
                        help='print available waveform types in this example')
    parser.add_argument('-w', '--waveform', default='SINE', nargs='+',
                        help='audio files')
    parser.add_argument('-d', '--device', default='', help='device name')
    parser.add_argument('-l', '--duration', default=30, type=int,
                        help='duration, in second')
    args = parser.parse_args()
    play(args.device, args.waveform, args.duration)
