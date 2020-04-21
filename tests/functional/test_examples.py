# Functional pytest module
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

from subprocess import run
from sys import executable

EVENT = './palace-event.py'
HRTF = './palace-hrtf.py'
INFO = './palace-info.py'
LATENCY = './palace-latency.py'
REVERB = '/palace-reverb.py'
STDEC = './palace-stdec.py'
TONEGEN = '/palace-tonegen.py'
WAVEFORMS = ['sine', 'square', 'sawtooth',
             'triangle', 'impulse', 'white-noise']


def test_event():
    event = run([executable, EVENT, WAV], capture_output=True)
    assert 'Opened' in event.stdout
    assert 'Playing' in event.stdout


def test_hrtf():
    hrtf = run([executable, HRTF, WAV], capture_output=True)
    assert 'Opened' in hrtf.stdout
    assert 'Playing' in hrtf.stdout


def test_info():
    info = run([executable, INFO], capture_output=True)
    assert 'Available basic devices' in info.stdout
    assert 'Available devices' in info.stdout
    assert 'Available capture devices' in info.stdout
    assert 'Info of device' in info.stdout
    assert 'ALC version' in info.stdout
    assert 'Available resamplers' in info.stdout
    assert 'EFX version' in info.stdout
    assert 'Max auxiliary sends' in info.stdout
    assert 'with the first being default' in info.stdout


def test_latency():
    latency = run([executable, LATENCY, WAV], capture_output=True)
    assert 'Opened' in latency.stdout
    assert 'Playing' in latency.stdout
    assert 'Offset' in latency.stdout


def test_reverb():
    reverbs = run([executable, REVERB, '-p'], capture_output=True)
    assert 'Available reverb preset names:' in reverbs.stdout
    fxs = reverbs.stdout.split('\n')[1:]
    for fx in fxs:
        reverb = run([executable, REVERB, '-r', fx], capture_output=True)
        assert 'Opened' in reverb.stdout
        assert 'Playing' in reverb.stdout
        assert fx in reverb.stdout


def test_stdec():
    stdec = run([executable, STDEC, WAV], capture_output=True)
    assert 'Opened' in stdec.stdout
    assert 'Playing' in stdec.stdout


def test_tonegen():
    for waveform in WAVEFORMS:
        tonegen = run([executable, TONEGEN, '-w', waveform],
                      capture_output=True)
        assert 'Opened' in tonegen.stdout
        assert 'Playing' in tonegen.stdout
        assert waveform in tonegen.stdout
