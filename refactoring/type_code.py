from contextlib import redirect_stdout
import io

import pytest


class Shape:
    def __init__(self, shape):
        assert shape in ('circle', 'dot')
        self.shape = shape

    def draw(self):
        if self.shape == 'circle':
            print('o')
        elif self.shape == 'dot':
            print('.')


def test_circle():
    _test_output(shape=Shape('circle'), expected_output='o')

def test_dot():
    _test_output(shape=Shape('dot'), expected_output='.')

def _test_output(shape, expected_output):
    f = io.StringIO()
    with redirect_stdout(f):
        shape.draw()
    output = f.getvalue()
    assert output == expected_output+'\n'