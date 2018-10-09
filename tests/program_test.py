import sys
import os
import pytest
sys.path.append(os.path.join(os.path.dirname(__file__),
                             os.pardir, "inception"))
import program


def test_type_validate_path():
    result = program.validate_path('home')
    assert type(result) is bool
