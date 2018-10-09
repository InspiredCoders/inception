import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),
                             os.pardir, "inception"))
import core


def test_type_get_file_names():
    result = core.get_file_names(os.getcwd())
    assert type(result) is tuple


def test_notdir_get_file_names():
    result = core.get_file_names("test.txt")
    assert result is None
