#!/usr/bin/env python3
# HRTF rendering example using ALC_SOFT_HRTF extension
# Copyright (C) 2020  Nguyễn Gia Phong
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

import wave
from argparse import ArgumentParser
from datetime import datetime, timedelta
from itertools import count, takewhile
from sys import stderr
from time import sleep
from typing import Iterable, Tuple

from palace import BaseDecoder, Device, Context, Source

CHUNK_LEN: int = 12000
QUEUE_SIZE: int = 4
PERIOD: float = 0.025


class WaveDecoder(BaseDecoder):
    def __init__(self, file: str) -> None: self.wave = wave.open(file, 'r')

    @BaseDecoder.frequency.getter
    def frequency(self) -> int: return self.wave.getframerate()

    @BaseDecoder.channel_config.getter
    def channel_config(self) -> str:
        n = self.wave.getnchannels()
        if n == 1: return 'Mono'
        if n == 2: return 'Stereo'

    @BaseDecoder.sample_type.getter
    def sample_type(self) -> str:
        n = self.wave.getsampwidth()
        if n == 1: return 'Unsigned 8-bit'
        if n == 2: return 'Signed 16-bit'

    @BaseDecoder.length.getter
    def length(self) -> int: return self.wave.getnframes()

    def seek(self, pos: int) -> bool:
        try:
            self.wave.setpos(pos)
        except wave.Error:
            return False
        else:
            return True

    @BaseDecoder.loop_points.getter
    def loop_points(self) -> Tuple[int, int]: return 0, 0

    def read(self, count: int) -> bytes: return self.wave.readframes(count)


def pretty_time(seconds: float) -> str:
    """Return human-readably formatted time."""
    time = datetime.min + timedelta(seconds=seconds)
    if seconds < 3600: return time.strftime('%M:%S')
    return time.strftime('%H:%M:%S')


def play(files: Iterable[str], device: str) -> None:
    with Device(device, fail_safe=True) as dev:
        print('Opened', dev.name['full'])
        for filename in files:
            try:
                decoder = WaveDecoder(filename)
            except FileNotFoundError:
                stderr.write(f'Failed to open file: {filename}\n')
                continue
            with Context(dev) as ctx, Source(ctx) as src:
                decoder.play(src, CHUNK_LEN, QUEUE_SIZE)
                print(f'Playing {filename} ({decoder.sample_type},',
                      f'{decoder.channel_config}, {decoder.frequency} Hz)')

                for i in takewhile(lambda i: src.playing, count()):
                    print(f' {pretty_time(src.offset_seconds)} /'
                          f' {pretty_time(decoder.length_seconds)}',
                          end='\r', flush=True)
                    sleep(PERIOD)
                    ctx.update()
                print()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('files', nargs='+', help='WAV audio files')
    parser.add_argument('-d', '--device', default='', help='device name')
    args = parser.parse_args()
    play(args.files, args.device)
