from app.main import get_short
import unittest

def test_get_short():
    s = get_short()
    assert len(s) == 6
