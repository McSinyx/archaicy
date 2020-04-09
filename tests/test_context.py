# Source pytest module
# Copyright (C) 2020  Ngô Ngọc Đức Huy
# Copyright (C) 2020  Nguyễn Gia Phong
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

"""This pytest module tries to test the correctness of the class Context."""

from palace import current_context, Context, DistanceModel, MessageHandler


def test_with_context(device):
    """Test if `with` can be used to start a context
    and is destroyed properly.
    """
    with Context(device) as context:
        assert current_context() == context


def test_nested_context_manager(device):
    """Test if the context manager returns to the
    previous context.
    """
    with Context(device) as context:
        with Context(device): pass
        assert current_context() == context


def test_message_handler(device):
    """Test read-write property MessageHandler."""
    context = Context(device)
    assert type(context.message_handler) is MessageHandler
    message_handler_test = type('MessageHandlerTest', (MessageHandler,), {})()
    context.message_handler = message_handler_test
    assert context.message_handler is message_handler_test
    with context:
        assert current_context().message_handler is context.message_handler


def test_async_wake_interval(device):
    """Test read-write property async_wake_interval."""
    with Context(device) as context:
        context.async_wake_interval = 42
        assert context.async_wake_interval == 42


# THIS DOES NOT WORK, PLEASE HELP!

# def test_is_supported(device):
#     with Context(device) as context:
#         assert context == current_context()
#         with context:
#             MONO42 = context.is_supported("MONO", "42")


def test_available_resamplers(device):
    """Test available_resamplers"""
    with Context(device) as context:
        assert context == current_context()
        assert len(context.available_resamplers) >= 0


def test_default_resampler_index(device):
    """Test default_resampler_index"""
    with Context(device) as context:
        assert context == current_context()
        assert context.default_resampler_index >= 0


def test_doppler_factor(device):
    """Test write property doppler_factor."""
    with Context(device) as context:
        context.doppler_factor = 4/9


def test_speed_of_sound(device):
    """Test write property speed_of_sound."""
    with Context(device) as context:
        context.speed_of_sound = 5/7


def test_distance_model(device):
    with Context(device) as context:
        context.distance_model = DistanceModel.INVERSE_CLAMPED
        context.distance_model = DistanceModel.LINEAR_CLAMPED
        context.distance_model = DistanceModel.EXPONENT_CLAMPED
        context.distance_model = DistanceModel.INVERSE
        context.distance_model = DistanceModel.LINEAR
        context.distance_model = DistanceModel.EXPONENT
        context.distance_model = DistanceModel.NONE
