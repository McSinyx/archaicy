# Source pytest module
# Copyright (C) 2020  Ngô Xuân Minh
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

"""This pytest module tries to test the correctness of the class Listener."""

from palace import Listener
from pytest import raises

from math import inf


def test_gain(context):
    """Test write property gain."""
    Listener(context).gain = 5/7
    Listener(context).gain = 7/5
    Listener(context).gain = 0
    Listener(context).gain = inf
    with raises(ValueError): Listener(context).gain = -1


def test_position(context):
    """Test write property position."""
    Listener(context).position = (1, 0, 1)
    Listener(context).position = (1, 0, -1)
    Listener(context).position = (1, -1, 0)
    Listener(context).position = (1, 1, 0)
    Listener(context).position = (0, 0, 0)
    Listener(context).position = (1, 1, 1)


def test_velocity(context):
    """Test write property velocity."""
    Listener(context).velocity = (420, 0, 69)
    Listener(context).velocity = (69, 0, -420)
    Listener(context).velocity = (0, 420, -69)
    Listener(context).velocity = (0, 0, 42)
    Listener(context).velocity = (0, 0, 0)
    Listener(context).velocity = (420, 69, 420)


def test_orientaion(context):
    """Test write property orientation."""
    Listener(context).orientation = [(420, 0, 69), (0, 42, 0)]
    Listener(context).orientation = [(69, 0, -420), (0, -69, 420)]
    Listener(context).orientation = [(0, 420, -69), (420, -69, 69)]
    Listener(context).orientation = [(0, 0, 42), (-420, -420, 0)]
    Listener(context).orientation = [(0, 0, 0), (-420, -69, -69)]
    Listener(context).orientation = [(420, 69, 420), (69, -420, 0)]


def test_meters_per_unit(context):
    """Test write property meter_per_unit."""
    Listener(context).gain = 4/9
    Listener(context).gain = 9/4
    Listener(context).gain = 0
    Listener(context).gain = inf
    with raises(ValueError): Listener(context).gain = -1
