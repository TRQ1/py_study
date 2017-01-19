import pytest
from py_study.srcs.main.study.replace import *

def test_string_replace():
    assert str.replace('old', 'new') == 'new'
