#!/usr/bin/env python3
# Example for loopback
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

from argparse import ArgumentParser
from time import sleep
from typing import Tuple

from numpy import arange, float32, pi, sin
from palace import Buffer, Context, BaseDecoder, Device, channel_configs


class SineGenerator(BaseDecoder):
    """Generator of elementary signals."""
    def __init__(self, duration: float, frequency: float):
        self.func = lambda frames: sin(
            frames / self.frequency * pi * 2 * frequency)
        self.duration = duration
        self.start = 0

    @BaseDecoder.frequency.getter
    def frequency(self) -> int: return 44100

    @BaseDecoder.channel_config.getter
    def channel_config(self) -> str:
        return 'Mono'

    @BaseDecoder.sample_type.getter
    def sample_type(self) -> str:
        return '32-bit float'

    @BaseDecoder.length.getter
    def length(self) -> int: return int(self.duration * self.frequency)

    def seek(self, pos: int) -> bool: return False

    @BaseDecoder.loop_points.getter
    def loop_points(self) -> Tuple[int, int]: return 0, 0

    def read(self, count: int) -> bytes:
        stop = min(self.start + count, self.length)
        data = self.func(arange(self.start, stop))
        self.start = stop
        return data.astype(float32).tobytes()


def play(device: str, duration: float, frequency: float,
         channel_config: str) -> None:
    """Play a sine wave and loopback through a channel."""
    with Device(device) as dev, Context(dev):
        print('Opened', dev.name)
        dec = SineGenerator(duration, frequency)
        print(f'Loopback a sine signal at {frequency} Hz for {duration} s')
        with Buffer.from_decoder(dec, 'loopback') as buf:
            buf.channel_config = channel_config
            with buf.play():
                sleep(duration)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d', '--device', default='', help='device name')
    parser.add_argument('-l', '--duration', default=1.0, type=float,
                        help='duration in second, default to 1.0')
    parser.add_argument('-f', '--frequency', default=440.0, type=float,
                        help='wave frequency in hertz, default to 440.0')
    parser.add_argument('-c', '--channel-config', default='Mono',
                        choices=channel_configs,
                        help='channel config for loopback')
    args = parser.parse_args()
    play(args.device, args.duration, args.frequency, args.channel_config)
