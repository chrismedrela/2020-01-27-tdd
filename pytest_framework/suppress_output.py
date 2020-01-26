from contextlib import contextmanager
import io, sys

@contextmanager
def suppress_output():
    stdout = sys.stdout
    sys.stdout = None
    try:
        yield stdout
    finally:
        sys.stdout = stdout