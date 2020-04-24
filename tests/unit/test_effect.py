# Effect pytest module
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

"""This pytest module tries to test the correctness of the class Effect."""

from palace import Context, Effect
from pytest import raises

from math import inf


def test_gain(device):
    """Test write-only property `gain`."""
    with Context(device), Effect() as fx:
        fx.gain = 0
        fx.gain = 1
        fx.gain = 7/5
        fx.gain = 5/7
        with raises(ValueError): fx.gain = -1


def test_send_auto():
    """Test write-only property `send_auto`."""
    with Context(device), Effect() as fx:
        fx.send_auto = False
        fx.send_auto = True
        with raises(ValueError): fx.gain = None


def test_use_count():
    """Test read-only property `use_count`."""
    with Context(device), Effect() as fx:
        assert fx.use_count == len(fx.source_sends)


def test_reverb_preset():
    """Test write-only property `reverb_preset`."""
    with Context(device), Effect() as fx:
        fx.reverb_preset = 'GENERIC'
