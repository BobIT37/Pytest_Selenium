import pytest
import sys

@pytest.mark.xfail
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.xfail
def test_mac_2():
    assert False