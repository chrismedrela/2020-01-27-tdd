import pytest

from contextlib import contextmanager
import io, sys

from suppress_output import suppress_output

def test_first():
    assert 1 == 0